from django.urls import path
from . import views

urlpatterns = [
    path('', views.choose_visitor, name='choose_visitor'),
    path('return-visitor/', views.return_visitor, name='return_visitor'),
    path('index/', views.index, name='index'),
    path('sign-out/', views.sign_out_view, name='sign_out')
    ]

