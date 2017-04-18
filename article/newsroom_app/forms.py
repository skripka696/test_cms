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
        field = self.cleaned_data['field']
        style_value = self.cleaned_data.get('style_value')
        style_instance = field.style.filter(style__id=self.cleaned_data.get('style').id)
        if style_instance.exists():
            field.style.remove(style_instance[0])
        if style_value:
            field.style.add(style_value)


class BaseArticleFormSet(BaseFormSet):
    def check_form_data(self, current_form, totals_forms):
        curr_cleaned_data = current_form.cleaned_data
        for form in totals_forms:
            if form == current_form:
                continue

            f1_cleaned_data = form.cleaned_data
            if curr_cleaned_data.get('style') == f1_cleaned_data.get('style'):
                return True
        return False

    def clean(self):
        if any(self.errors):
            return

        if self.total_form_count() > 1:
            for form in self.forms:
                if self.check_form_data(form, self.forms):
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
