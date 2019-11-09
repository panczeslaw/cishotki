from django import forms
from django.template.loader import render_to_string

class ColorWidget(forms.Widget):
    class Media:
        js = ['js/color.min.js']

    def render(self, name, value, attrs=None, renderer=None, **_kwargs):
        is_required = self.is_required
        return render_to_string('colorfield/color.html', locals())

    def value_from_datadict(self, data, files, name):
        ret = super(ColorWidget, self).value_from_datadict(data, files, name)
        ret = '#%s' % ret if ret else ret
        return ret