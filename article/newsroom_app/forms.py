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
                if key == 'style_value':
                    field.widget.attrs['disabled'] = 'disabled'
                    field.widget.attrs['class'] += ' style_option'
                else:
                    field.widget.attrs['class'] += ' style_name'
                field.widget.attrs['class'] += ' col-4'
            else:
                field.widget.attrs['class'] += ' col-11'

    def save(self):
        field = self.cleaned_data['field']
        style_value = self.cleaned_data['style_value']
        field.style.add(style_value)

AdminCreateStyleFormSet = formset_factory(AdminCreateStyle, extra=1)


