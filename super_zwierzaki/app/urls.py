from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^card/new/$', views.card_new, name='card_new'),
    url(r'^card/new/ok/$', views.index, name='ok'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/password/$', views.password, name='password'),
]