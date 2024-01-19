from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('sign-in/', views.signIn, name='sign-in'),
  path('sign-out/', views.signOut, name='sign-out'),
  path('dashboard/', views.dashboard, name='dashboard'),
]
