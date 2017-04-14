from django import forms
from django.forms import formset_factory
from newsroom_app.models import Field, Style, StyleValue


class AdminCreateStyle(forms.Form):
    field = forms.ModelChoiceField(queryset=Field.objects.all())
    style = forms.ModelChoiceField(queryset=Style.objects.all())
    style_value = forms.ModelChoiceField(queryset=StyleValue.objects.all())

    def __init__(self, *args, **kwargs):
        super(AdminCreateStyle, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control form_field'
            if key != 'field':
                field.widget.attrs['class'] += ' col-4'
            else:
                field.widget.attrs['class'] += ' col-12'


AdminCreateStyleFormSet = formset_factory(AdminCreateStyle, extra=1)


