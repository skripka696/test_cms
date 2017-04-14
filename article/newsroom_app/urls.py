from django.conf.urls import url
from newsroom_app import views

urlpatterns = [
    url(r'^create_style/$', views.CreateStyle.as_view(), name='add_style'),
]
