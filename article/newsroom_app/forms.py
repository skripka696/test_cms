from django import forms
from django.forms import formset_factory
from django.forms.formsets import BaseFormSet
from newsroom_app.models import Field, Style, Article, StyleValue, ArticleContent


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
        style_value = self.cleaned_data.get('style_value')
        style_instance = Field.objects.filter(style__style__name=self.cleaned_data.get('style'))
        field = self.cleaned_data.get('field')
        if style_instance:
            field.style.remove()
        if style_value:
            field.style.add(style_value)


class BaseArticleFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return

        if self.total_form_count() > 1:
            for i in range(0, self.total_form_count()):
                f1_cleaned_data = self.forms[i].cleaned_data
                for j in range(0, self.total_form_count()):
                    f2_cleaned_data = self.forms[j].cleaned_data
                    if f1_cleaned_data.get('style') and f2_cleaned_data.get('style'):
                        if f1_cleaned_data.get('style') == f2_cleaned_data.get('style'):
                            raise forms.ValidationError('You choosed two or more equal styles')


AdminCreateStyleFormSet = formset_factory(AdminCreateStyle,
                                          formset=BaseArticleFormSet,
                                          extra=1)


class CreateArticleForm(forms.Form):
    status = forms.ChoiceField(label='Status', choices=Article.STATUS_CHOICES)
    access = forms.ChoiceField(label='Access', choices=Article.ACCESS_CHOICES)
    field_text = forms.ModelChoiceField(queryset=Field.objects.all())
    text_value = forms.CharField(widget=forms.Textarea)

    class Meta:
        models = Article
        fields = ('status', 'access', 'field_text', 'text_value')

    def __init__(self, *args, **kwargs):
        super(CreateArticleForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs['class'] = 'form-control form_field'
        self.fields['access'].widget.attrs['class'] = 'form-control form_field'
        self.fields['field_text'].widget.attrs['class'] = 'form-control form_field'
        self.fields['text_value'].widget.attrs['class'] = 'form-control form_field mytextarea'
        # for key, field in self.fields.items():
        #     field.widget.attrs['class'] = 'form-control form_field'
