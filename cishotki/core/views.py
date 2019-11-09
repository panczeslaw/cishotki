from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .forms import ConstructorForm

def main(request):
	data = {
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