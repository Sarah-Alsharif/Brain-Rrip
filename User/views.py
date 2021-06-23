from django.shortcuts import render , redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect

# Create your views here.


def signup(request):
    form = UserForm()
    if (request.method == "POST"):
        user = UserForm(request.POST)
        if (user.is_valid()):
            user.save()
            messages.add_message(request , messages.SUCCESS , "You have been successfully registered, please complete your profile")
            return redirect('home')
        else:
            form = user
    return render(request , 'signup.html' , 
    {
        "form" : form
    }
    )

def profile(request):
    print("from profile")
    return render(request , 'profile.html')


# update profile
def update_profile(request,pk):
    update_profile= Profile.objects.get(pk=pk)
    form = ProfileForm(instance=update_profile)

    if (request.method == "POST"):
        Updated_profile =ProfileForm(request.POST, request.FILES, instance=update_profile) 
        if Updated_profile.is_valid() :
            Updated_profile.save()
            return redirect ('profile')
    
    return render(request, 'profileForm.html' , {'form' : form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            #update_session_auth_hash(request, user)  # Important!
            request.user = user 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })
    
    
def mycourses(request):
    print(request.user)
    print(request.user.mycourses.all())
    print(request.user.courses.all())
    return render(request, 'myCourses.html')
    