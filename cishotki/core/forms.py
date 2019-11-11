from django import forms
from cishotki.settings import SEX, SIZES

from django.utils.translation import ugettext as _
from django.core.validators import RegexValidator
from django.contrib.admin.widgets import FilteredSelectMultiple, RelatedFieldWidgetWrapper
from django.core.files.images import get_image_dimensions

from django_select2.forms import Select2MultipleWidget

from .widgets import ColorWidget, CustomSelect2TagWidget

from tshirts.models import Topic, Tag

import re

color_re = re.compile('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')
validate_color = RegexValidator(color_re, _('Enter a valid color.'), 'invalid')

def validate_image(image):
    x, y = get_image_dimensions(image.file)
    if x < 1000 or y < 1000:
        raise ValidationError(_("Image size must exceed 1000px in each dimension"))


class ConstructorForm(forms.Form):
	TYPE_CHOICES = (
		("pattern", _("Pattern")),
		("color", _("Color and picture")),
	)

	name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": " bg-transparent text-light form-control form-control-light"}), required=True)
	description = forms.CharField(max_length=500, widget=forms.Textarea(attrs={"class": "bg-transparent text-light form-control form-control-light"}), required=True)
	sex = forms.ChoiceField(choices=SEX, widget=forms.RadioSelect(attrs={"class": "bg-transparent text-light custom-control-input"}), required=True)
	background = forms.CharField(required=False, widget=ColorWidget(), validators=[validate_color,])
	file = forms.ImageField(required=False, validators=[validate_image])
	is_pattern = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "text-light custom-control-input"}))
	topic = forms.ModelMultipleChoiceField(
		widget=Select2MultipleWidget(attrs={"class": "form-control form-control-light"}),
		queryset=Topic.objects.all(), 
		required=True,
	)
	tag = forms.ModelMultipleChoiceField(
		widget=CustomSelect2TagWidget(attrs={"class": "bg-transparent text-light form-control form-control-light"}), 
		queryset=Tag.objects.all(),
		required=True
	)
