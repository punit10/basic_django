from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('help/', views.help, name='help'),
    path('users/', views.users, name='users'),
    # path('user_form/', views.user_form_view, name='user_form')
    path('user_form/', views.users, name='user_form')

]
