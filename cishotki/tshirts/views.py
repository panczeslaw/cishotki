from django.shortcuts import render

from django.http import HttpResponse

from django.views import View

class TShirtsView(View):
	def get(self, request):
		return HttpResponse("Макс иди нахуй")