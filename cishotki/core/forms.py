from django import forms
from cishotki.settings import SEX, SIZES

from django.utils.translation import ugettext as _
from django.core.validators import RegexValidator

from .widgets import ColorWidget


import re

color_re = re.compile('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
validate_color = RegexValidator(color_re, _('Enter a valid color.'), 'invalid')


class ConstructorForm(forms.Form):
	TYPE_CHOICES = (
		("pattern", _("Pattern")),
		("color", _("Color and picture")),
	)

	sex = forms.ChoiceField(choices=SEX, widget=forms.RadioSelect(attrs={"class": "text-light custom-control-input"}))
	background = forms.CharField(widget=ColorWidget(), validators=[validate_color,])
	file = forms.ImageField()
	#is_file_pattern = forms.(widget=forms.CheckboxInput(attrs={"class": "text-light custom-control-input"}))