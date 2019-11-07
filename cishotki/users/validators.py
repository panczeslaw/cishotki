from django.forms import ValidationError
from django.utils.translation import ugettext as _

from django.core.exceptions import ObjectDoesNotExist

from .models import User

def validate_username(value):
	try:
		u = User.objects.get(username=value)
	except ObjectDoesNotExist:
		pass
	else:
		raise ValidationError(_("A user with that username already exists."))

def validate_unique_email(value):
	try:
		у = User.objects.get(email=value)
	except ObjectDoesNotExist:
		pass
	else:
		raise ValidationError(_("A user with that e-mail already exists."))

