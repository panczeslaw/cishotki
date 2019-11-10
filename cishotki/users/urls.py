from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from cishotki.settings import THEME

from .forms import CustomAuthenticationForm, CustomSetPasswordForm
from .views import RegisterView, ActivateAccountView, ProfileView, DesignsView

urlpatterns = [
	path("login/", LoginView.as_view(
		template_name="users/login.html",
		redirect_authenticated_user=True,
		authentication_form=CustomAuthenticationForm,
	), name="login"),
	path("logout/", LogoutView.as_view(), name="logout"),
	path("register/", RegisterView.as_view(), name="register"),
	path("activate/<str:hash>", ActivateAccountView.as_view(), name="activate_account"),
	path("reset/", PasswordResetView.as_view(
		template_name="users/login.html",
	), name="password_reset"),
	path("reset/requested/", PasswordResetDoneView.as_view(
		template_name="users/password_reset_requested.html",
	), name="password_reset_done"),
	path("reset/confirm/<str:uidb64>/<str:token>", PasswordResetConfirmView.as_view(
		template_name="users/password_change.html",
		form_class=CustomSetPasswordForm,
		post_reset_login=True,
	), name="password_reset_confirm"),
	path("reset/complete", PasswordResetCompleteView.as_view(
		template_name="users/password_reset_complete.html",
	), name="password_reset_complete"),
	path("profile/", ProfileView.as_view(), name="profile"),
	path("designs/", DesignsView.as_view(),  name="designs"),
]