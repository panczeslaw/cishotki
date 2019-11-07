from django.shortcuts import render

from django.utils import translation

from cishotki.settings import THEME


def main(request):
	translation.activate('en')
	data = {
		"theme": THEME
	}
	return render(request, "core/main.html", context=data)




def about(request):
	translation.activate('en')
	data = {
		"theme": THEME
	}
	return render(request, "core/main.html", context=data)