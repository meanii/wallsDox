from django.urls import path 
from . import views

urlpatterns = [
    path('', views.account_view, name='accounts'),
    path('logout', views.logout_view, name='logout')
  ]