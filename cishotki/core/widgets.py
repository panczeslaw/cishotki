from django import forms
from django.template.loader import render_to_string

from django_select2.forms import ModelSelect2TagWidget


from tshirts.models import Tag

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


class CustomSelect2TagWidget(ModelSelect2TagWidget):
    queryset = Tag.objects.all()
    search_fields = ["tag"]

    def value_from_datadict(self, data, files, name):
        value = super().value_from_datadict(data, files, name)
        values_ids = []
        for i in value:
            try:
                x = int(i)
            except ValueError:
                pass
            else:
                values_ids.append(i)
        qs = self.queryset.filter(**{'pk__in': list(values_ids)})
        pks = set(str(getattr(o, 'id')) for o in qs)
        cleaned_values = []
        for val in value:
            if str(val) not in pks:
                val = self.queryset.create(tag=val).id
            cleaned_values.append(val)
        return cleaned_values