from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from cishotki.settings import THEME

from .forms import CustomAuthenticationForm
from .views import RegisterView, ActivateAccountView

urlpatterns = [
	path("login/", LoginView.as_view(
		template_name="users/login.html",
		extra_context={"theme": THEME},
		redirect_authenticated_user=True,
		authentication_form=CustomAuthenticationForm,
	), name="login"),
	path("logout/", LogoutView.as_view(), name="logout"),
	path("register/", RegisterView.as_view(), name="register"),
	path("activate/<str:hash>", ActivateAccountView.as_view(), name="activate_account"),
]