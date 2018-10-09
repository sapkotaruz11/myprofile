from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'projects/', views.projects, name='projects'),
    url(r'home/',views.home, name='home'),
    url(r'resume/',views.resume, name='resume'),
    url(r'about/',views.about, name='about'),
]
