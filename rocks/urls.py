from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^detail/(?P<rock_name>[äöü,\sa-zA-Z()-]+)/$', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
]
