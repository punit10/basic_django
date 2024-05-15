from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import Users
from . import forms

# Create your views here.
def index(request):
    # return HttpResponse("<em>Welcome to Second Project, go to /users</em>")
    index_dict = {'index_insert':'INDEX PAGE'}
    return render(request,'appTwo/index.html',context=index_dict)

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'appTwo/help.html',context=helpdict)

def users(request):
    users_list = Users.objects.order_by('id')
    user_dict = {'users': users_list}
    return render(request, 'appTwo/users.html', context=user_dict)

def user_form_view(request):
    form = forms.UserForm()
    if request.method == "POST":
        form = forms.UserForm(request.POST)

        if form.is_valid():
            print("Validation success!")
            print(form.cleaned_data['name'])
            # print("Name: " + form.changed_data['name'])
            # print("email: " + form.changed_data['email'])
            # print("address: " + form.changed_data['address'])


    return render(request, 'appTwo/user_form.html', {'form': form})