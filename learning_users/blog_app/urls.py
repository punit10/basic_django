# from django.conf.urls import url
from blog_app import views
from django.urls import path

# TEMPLATE TAGGING
app_name = 'blog_app'

urlpatterns = [
    path('', views.index, name='blog_app_index'),
    path('register/', views.register, name='register')
]
