from django.urls import path
from . import views

urlpatterns = [
    # path('', views.help, name='help'),
    path('', views.users, name='users'),
]
