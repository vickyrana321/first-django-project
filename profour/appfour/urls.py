from django.conf.urls import url

from appfour import views

app_name = 'appfour'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),


]