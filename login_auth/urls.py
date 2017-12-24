from django.conf.urls import url
from . import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^register/', views.register, name='register'),
]