from django.conf.urls import url
from user_profile import views
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^registration/$', views.Registration.as_view(), name='registr'),
]