from django.conf.urls import patterns, url

from web import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^create/$', views.create, name='create'),
    url(r'^created/$', views.created, name='created'),
    url(r'^note/$', views.note, name='note'),
)