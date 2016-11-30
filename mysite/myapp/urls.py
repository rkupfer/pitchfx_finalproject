from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^form/$', views.form, name ='form'),
    url(r'^formclass/$', views.FormClass.as_view(), name = "formclass"),
    url(r'^plot/$', views.plot, name='plot'),
    url(r'^ourdata/$', views.our_data, name='our data')
]
