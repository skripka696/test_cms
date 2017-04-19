from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.http.response import JsonResponse, HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic import FormView
from django.views.generic.list import ListView
from newsroom_app.models import StyleValue, Field, ArticleContent
from newsroom_app.forms import AdminCreateStyleFormSet

from newsroom_app.forms import CreateArticleForm
from newsroom_app.models import Article


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
                    return self.render_to_response(self.get_context_data())
            return HttpResponseRedirect(reverse_lazy('style_list'))
        else:
            return self.render_to_response(self.get_context_data(form=formset))

    def get_context_data(self, **kwargs):
        context = super(CreateStyle, self).get_context_data(**kwargs)
        return context


class StyleListView(ListView):
    model = Field
    template_name = 'style_list.html'


@login_required
def get_style_options(request, id):
    styles_options = StyleValue.objects.filter(style__id=id)
    return JsonResponse({
        'data': [model_to_dict(style_options) for style_options in styles_options]
    })

#
# @login_required
# def get_field_style(request):
#     styles = Field.objects.all()
#     style_data = {
#         'title': {},
#         'main content': {},
#     }
#     for style in styles:
#         t = {}
#         for item in style.style.all():
#             t[item.style.name] = item.value
#         if t:
#             style_data[style.description] = t
#
#     return JsonResponse(style_data)


class CreateArticle(FormView):
    model = Article
    template_name = 'create_article.html'
    form_class = CreateArticleForm

    def post(self, request, *args, **kwargs):
        return HttpResponse()

    def get_context_data(self, **kwargs):
        context = super(CreateArticle, self).get_context_data(**kwargs)
        return context
