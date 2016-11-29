from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^plot/$', views.plot, name='plot')]
