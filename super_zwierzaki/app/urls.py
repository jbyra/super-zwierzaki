from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^card/new/$', views.card_new, name='card_new'),
    url(r'^card/new/ok/$', views.index, name='ok')
]