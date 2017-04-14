from django import forms
from django.forms import formset_factory
from django.forms.formsets import BaseFormSet
from newsroom_app.models import Field, Style, StyleValue, ArticleContent


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
        style_value = self.cleaned_data['style_value']
        style_instance = Field.objects.filter(style__style__name=self.cleaned_data['style'])
        field = self.cleaned_data['field']
        if style_instance:
            field.style.remove()
        field.style.add(style_value)


class BaseArticleFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return

        for i in range(0, self.total_form_count()):
            f1_cleaned_data = self.forms[i].cleaned_data
            for j in range(0, self.total_form_count()):
                f2_cleaned_data = self.forms[j].cleaned_data
                if f1_cleaned_data['style'] == f2_cleaned_data['style']:
                    raise forms.ValidationError('You choosed two or more equal styles')


AdminCreateStyleFormSet = formset_factory(AdminCreateStyle,
                                          formset=BaseArticleFormSet,
                                          extra=1)


class CreateArticle(forms.Form):
    class Meta:
        models = ArticleContent
        fields = '__all__'