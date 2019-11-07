from django.contrib.auth.forms import AuthenticationForm
from django.forms import ValidationError, widgets
from django import forms

from django.utils.translation import ugettext as _
from django.contrib.auth.password_validation import validate_password

from .validators import validate_username, validate_unique_email

from django.core.validators import validate_email


class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                _("This account is inactive."),
                code='inactive',
            )
        if user.is_banned:
            raise ValidationError(
                _("This account banned due to violations of our non-existing site rules."),
                code="banned",
            )

        if not user.is_confirmed:
            raise ValidationError(
                _("Your account is not confirmed. Please check your e-mail for the letter with activation link."),
                code="banned",
            )

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=32, required=True, validators=[validate_username,])
    first_name = forms.CharField(max_length=32, required=True)
    last_name = forms.CharField(max_length=32, required=True)
    email = forms.EmailField(required=True, validators=[validate_email, validate_unique_email,])
    password = forms.CharField(max_length=32, required=True, widget=widgets.PasswordInput(), validators=[validate_password,])
    