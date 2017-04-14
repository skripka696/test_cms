from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import FormView
from newsroom_app.models import StyleValue, Field
from newsroom_app.forms import AdminCreateStyleFormSet


class CreateStyle(FormView):
    model = Field
    template_name = 'admin_create_style.html'
    form_class = AdminCreateStyleFormSet

    def post(self, request, *args, **kwargs):
        return HttpResponse()

    def get_context_data(self, **kwargs):
        context = super(CreateStyle, self).get_context_data(**kwargs)
        return context
    # def get(self, request, *args, **kwargs):
    #     fields = Field.objects.all()
    #     # styles = StyleValue.objects.all()
    #     context = {'fields': fields}
    #
    #     return render(request, self.template_name, context)


