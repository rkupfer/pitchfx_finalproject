from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [
    url(r'^$', views.form, name = 'form'),
    url(r'^form2/$', views.form2, name ='form2'),
    url(r'^formclass/$', views.FormClass.as_view(), name = "formclass"),
    url(r'^ourdata/$', views.our_data, name='our data')
]
