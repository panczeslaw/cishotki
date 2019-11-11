from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .forms import ConstructorForm
from tshirts.models import Topic, Tag, TShirt, Rate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .forms import ConstructorForm

from PIL import Image, ImageDraw, ImageChops

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

			if not is_pattern:
				imPR = Image.open(form.cleaned_data["file"])

				ratio = (imPR.size[0] / 250)

				r_imPR = imPR.resize((250, int(imPR.size[1] / ratio)))

				pos = (500 - r_imPR.size[0] // 2, 500 - r_imPR.size[1] // 2)
				im.paste(r_imPR, pos)

			im.save("temp/temp.png")
			im.show()

			return HttpResponse("OK")
		else:
			data = {
				"form": form,
			}
			return render(request, "core/constructor.html", context=data)
