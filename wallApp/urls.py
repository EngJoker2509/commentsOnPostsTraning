from django.urls import path
from . import views

app_name='Thewall'

urlpatterns=[
    path('',views.index,name='index'),
    path('wall',views.wall,name='wall'),
    path('destroy',views.destroy,name='destroy'),
]