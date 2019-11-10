from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .forms import ConstructorForm
from tshirts.models import Topic, Tag, TShirt, Rate


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