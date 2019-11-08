from django.shortcuts import render

from django.utils import translation


def main(request):
	data = {
	}
	return render(request, "core/main.html", context=data)




def about(request):
	data = {
	}
	return render(request, "core/main.html", context=data)