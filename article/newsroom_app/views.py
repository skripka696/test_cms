from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import FormView
from newsroom_app.models import StyleValue, Field, ArticleContent
from newsroom_app.forms import AdminCreateStyleFormSet


class CreateStyle(FormView):
    model = Field
    template_name = 'admin_create_style.html'
    form_class = AdminCreateStyleFormSet

    def post(self, request, *args, **kwargs):
        formset = AdminCreateStyleFormSet(request.POST)
        if formset.is_valid():
            for form in formset.forms:
                if form.is_valid():
                    form.save()
                else:
                    return self.render_to_response(formset.get_context_data())
            return HttpResponse()
        else:
            return self.render_to_response(formset.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(CreateStyle, self).get_context_data(**kwargs)
        return context


class CreateArticle(FormView):
    model = ArticleContent
    template_name = 'create_article.html'

    def post(self, request, *args, **kwargs):
        return HttpResponse()

    def get_context_data(self, **kwargs):
        context = super(CreateArticle, self).get_context_data(**kwargs)
        return context