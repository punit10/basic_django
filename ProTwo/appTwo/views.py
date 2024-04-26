from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import Users

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