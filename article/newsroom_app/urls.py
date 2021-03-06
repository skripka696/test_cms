from django.conf.urls import url
from newsroom_app import views

urlpatterns = [
    url(r'^create_style/$', views.CreateStyle.as_view(), name='add_style'),
    url(r'^get_style_options/(?P<id>\d+)/$', views.get_style_options, name='get_style_options'),
    url(r'^create_article/$', views.CreateArticle.as_view(), name='add_style'),
    url(r'^style-list/$', views.StyleListView.as_view(), name='style_list'),
]
