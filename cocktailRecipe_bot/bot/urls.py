# from django.conf.urls import url, include, path
from django.urls import path
from . import views

# use to connect callback main program
urlpatterns = [
    path('callback/', views.callback, name='callback')
]
