from django.shortcuts import render
from blog_app.forms import UserForm, UserProfileInfoForm
from django.http import HttpResponse
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
