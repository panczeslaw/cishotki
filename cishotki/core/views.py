from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from django.core.files import File

from .forms import ConstructorForm
from tshirts.models import Topic, Tag, TShirt, Rate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .forms import ConstructorForm

from PIL import Image, ImageDraw, ImageChops

from cloudinary import CloudinaryResource


import cloudinary

def main(request):
	tshirts = TShirt.objects.all()
	data = {
	    "tshirts": tshirts
	}
	return render(request, "core/main.html", context=data)


def about(request):
	data = {
	}
	return render(request, "core/main.html", context=data)


class ConstructorView(LoginRequiredMixin, View):
	def get(self, request):
		data = {
			"form": ConstructorForm(),
		}
		return render(request, "core/constructor.html", context=data)

	def post(self, request):
		form = ConstructorForm(request.POST, request.FILES)
		if form.is_valid():
			im = Image.open("static/img/template-{}.png".format(form.cleaned_data["sex"]))
			is_pattern = form.cleaned_data["is_pattern"]
			print(is_pattern)
			bg = form.cleaned_data["background"]
			if is_pattern:
				imP = Image.open(form.cleaned_data["file"])
				
				width, height = imP.size   # Get dimensions

				left = (width - 1000) / 2
				top = (height - 1000) / 2
				right = (width + 1000) / 2
				bottom = (height + 1000) / 2

				imP = imP.crop((left, top, right, bottom))
			else:
				imP = Image.new("RGBA", size=(1000, 1000), color=(int(bg[1:3], 16), int(bg[3:5], 16), int(bg[5:7], 16), 255))
			
			imP.paste(im, (0, 0), im)
			
			im = imP.copy()

			if not is_pattern and form.cleaned_data["file"]:
				imPR = Image.open(form.cleaned_data["file"])

				ratio = (imPR.size[0] / 250)

				r_imPR = imPR.resize((250, int(imPR.size[1] / ratio)))

				pos = (500 - r_imPR.size[0] // 2, 500 - r_imPR.size[1] // 2)
				im.paste(r_imPR, pos)

			im.save("temp/temp.png")

			resp = cloudinary.uploader.upload('temp/temp.png')
			result = CloudinaryResource(
				public_id=resp['public_id'],
				type=resp['type'],
				resource_type=resp['resource_type'],
				version=resp['version'],
				format=resp['format'],
			)

			str_result = result.get_prep_value()

			if request.FILES:
				resp2 = cloudinary.uploader.upload(File.open(request.FILES["file"], "rb"))
				result2 = CloudinaryResource(
					public_id=resp2['public_id'],
					type=resp2['type'],
					resource_type=resp2['resource_type'],
					version=resp2['version'],
					format=resp2['format'],
				)
				str_result2 = result2.get_prep_value()
			else:
				str_result2 = None


			tshirt = TShirt.objects.create(
				user=request.user,
				name=form.cleaned_data["name"],
				description=form.cleaned_data["description"],
				image=str_result,
				sex=form.cleaned_data["sex"],
				uploaded_image=str_result2,
				background=form.cleaned_data["background"],
				is_pattern=form.cleaned_data["is_pattern"],
			)
			tshirt.topic.set(form.cleaned_data["topic"])
			tshirt.tag.set(form.cleaned_data["tag"])
	


			return redirect('design_view', tshirt_id=tshirt.id)
		else:
			data = {
				"form": form,
			}
			return render(request, "core/constructor.html", context=data)





class OrderView(View):

	def get(self, request, sign):

		order = get_object_or_404(Order, sign=sign)
		
		form = OrderForm({
			"wsb_storeid": WSB_STORE_ID,
			"wsb_store": WSB_STORE_NAME,
			"wsb_test": WSB_TEST,
			"wsb_version": WSB_VERSION,
			"wsb_currency_id": WSB_CURRENCY,
			"wsb_order_num": order.id,
			"wsb_seed": order.seed,
			"wsb_signature": order.sign,
			"wsb_return_url": "http{}://{}{}".format("s" if request.is_secure() else "", request.get_host(), reverse('successorderview', args=[order.sign])),
			"wsb_cancel_return_url": "http{}://{}{}".format("s" if request.is_secure() else "", request.get_host(), reverse('cancelorderview', args=[order.sign])),
			"wsb_notify_url": "http{}://{}{}".format("s" if request.is_secure() else "", request.get_host(), reverse('orderview', args=[order.sign])),
			"wsb_customer_name": order.full_name,
			"wsb_total": order.cost,
			"wsb_email": order.email,
		})
		data = {
			"form": form,
			"webpay_host": WEBPAY_HOST,
			"order": order,
		}
		return render(request, "core/precheckout.html", data)

	def post(self, request, sign):
		order = get_object_or_404(Order, sign=sign)
		order.webpay_transaction_id = check_signature(request.POST)
		order.save()
		return HttpResponse("Ok!")



class CancelOrderView(View):

	def get(self, request, sign):

		order = get_object_or_404(Order, sign=sign)

		return HttpResponse("Cancelled")


class SuccessOrderView(View):

	def get(self, request, sign):

		order = get_object_or_404(Order, sign=sign)
		return HttpResponse("OK")
		