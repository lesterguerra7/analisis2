from django.conf.urls import patterns, url
from registro import views
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)