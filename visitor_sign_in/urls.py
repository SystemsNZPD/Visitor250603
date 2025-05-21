from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('return-visitor/', views.return_visitor, name='return_visitor'),
    ]

