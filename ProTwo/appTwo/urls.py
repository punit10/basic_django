from django.urls import path
from . import views

#TEMPLATE TAGGING
app_name = 'apptwo'

urlpatterns = [
    path('help/', views.help, name='help'),
    path('users/', views.users, name='users'),
    # path('user_form/', views.user_form_view, name='user_form'),
    path('user_form/', views.users, name='user_form'),

    path('', views.apptwo_index, name='apptwo_index'),
    path('other/', views.other_page, name='other'),
    path('relative/', views.relative_url_templates, name='relative')

]
