from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.views.generic.edit import FormView


class UserForm(UserCreationForm):
    password1 = forms.CharField(help_text='Please make your password hrader to crack', widget=forms.PasswordInput())
    username=forms.CharField(max_length=30, help_text="Use letters, digits and special character only.")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', )


#class PasswordResetConfirmView(FormView):

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user']
