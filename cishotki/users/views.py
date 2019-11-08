from django.shortcuts import render, redirect, get_object_or_404

from django.views import View

from django.http import HttpResponse

from cishotki.settings import EMAIL_HOST_USER
from .forms import RegisterForm
from .models import User
from django.core.mail import send_mail
from django.contrib.auth import login

from django.utils.translation import ugettext as _



class RegisterView(View):
	def get(self, request):
		return render(request, "users/login.html")

	def post(self, request):
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				username=form.cleaned_data["username"],
				password=form.cleaned_data["password"],
				email=form.cleaned_data["email"],
			)
			user.first_name = form.cleaned_data["first_name"]
			user.last_name = form.cleaned_data["last_name"]
			user.save()
			user.setup_confirmation()
			send_mail(
				_("E-mail confirmation on cishotki.by"),
				_("Hi, {first_name}! Please confirm you e-mail by following this link: {url}").format(
					first_name=user.first_name,
					url="http{}://{}/accounts/activate/{}".format(
						"s" if request.is_secure() else "",
						request.get_host(), 
						user.confirmation_hash,
					),
				),
				EMAIL_HOST_USER,
				[user.email],
				fail_silently=False
			)

			return HttpResponse("Проверь почту, чмо")
		data = {
			"form": form,
		}
		return render(request, "users/login.html", context=data)



class ActivateAccountView(View):
	def get(self, request, hash):
		user = get_object_or_404(User, confirmation_hash=hash)
		user.is_confirmed = True
		user.save()
		login(request, user)
		return render(request, "users/email_confirmed.html")