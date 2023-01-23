from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('',views.form_page),
    path('register',views.register),
    path('login',views.login),
    path('clear',views.clear,name='clear')
]