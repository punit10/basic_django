from django.shortcuts import render
from blog_app.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    context_dict = {"name": 'Hello World'}
    return render(request, 'blog_app/index.html', context_dict)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    # else of request.method
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'blog_app/registration.html',
           {'user_form': user_form,
                    'profile_form': profile_form,
                    'registered': registered})


# views name should not match anything we have imported like login, authenticate etc
def user_login(request):

    if request.method == 'POST':
        filled_username = request.POST.get('username')
        filled_password = request.POST.get('password')

        # builtin automatic authenticate user, and checks login by login() method. Thanks django
        user = authenticate(username=filled_username, password=filled_password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE! Contact Admin!")

        else:
            print("Someone tried login and failed!")
            print("Username {} and Password {}", format(filled_username, filled_password))
            return HttpResponse('INVALID CREDENTIALS!')

    else:
        return render(request, 'blog_app/login.html', {})


@login_required   # decorator function checks only logged-in users can log out
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required()
def booking(request):
    return HttpResponse("You are Logged in. Enjoy!")
