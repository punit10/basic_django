from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import Users
from appTwo.forms import NewUserForm
from . import forms

# Create your views here.
def index(request):
    # return HttpResponse("<em>Welcome to Second Project, go to /users</em>")
    index_dict = {'index_insert':'INDEX PAGE'}
    return render(request,'appTwo/index.html',context=index_dict)


def apptwo_index(request):
    index_dict = {'address': 'Company address is two horizon center, Gurgaon', 'employees': 2000}
    return render(request,'appTwo/apptwo_index.html',context=index_dict)

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'appTwo/help.html',context=helpdict)

def users(request):
    # users_list = Users.objects.order_by('id')
    # user_dict = {'users': users_list}
    # return render(request, 'appTwo/users.html', context=user_dict)
    
    #creating form by model forms
    form = NewUserForm(request.POST)
    if request.method == 'Post':
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('INVALID FORM')

    return render(request, 'appTwo/user_form.html', {'form':form})        

def user_form_view(request):
    form = forms.NewUserForm()
    if request.method == "POST":
        form = forms.NewUserForm(request.POST)

        if form.is_valid():
            print("Validation success!")
            print(form.cleaned_data['name'])
            # print("Name: " + form.changed_data['name'])
            # print("email: " + form.changed_data['email'])
            # print("address: " + form.changed_data['address'])


    return render(request, 'appTwo/user_form.html', {'form': form})

def other_page(request):
    return render(request, 'appTwo/other.html')

def base(request):
    return render(request, 'appTwo/base.html')

def relative_url_templates(request):
    return render(request, 'appTwo/relative_url_templates.html')