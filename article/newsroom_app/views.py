from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.generic import FormView
from newsroom_app.models import StyleValue, Field
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


@login_required
def get_style_options(request, id):
    styles_options = StyleValue.objects.filter(style__id=id)
    return JsonResponse({
        'data': [model_to_dict(style_options) for style_options in styles_options]
    })
