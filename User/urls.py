from django.urls import path
from django.contrib.auth import views as as_view
from django.contrib.auth import views as auth_views

from User import views

urlpatterns = [
    path('login/' , as_view.LoginView.as_view(template_name = "login.html") , name= "login"),
    path('logout/' , as_view.LogoutView.as_view() , name = "logout"),
    path('signup/' , views.signup, name = "signup"),
    path('profile/' , views.profile , name="profile" ),
    path('profile/<pk>/update' , views.update_profile , name="profileUpdate"),  
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_resetform.html"), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),
    path('change_password', views.change_password, name='change_password'),
    path('mycourses', views.mycourses, name='mycourses'),
]
"""
1- submit email form 
2- email success message
3- link password reset form
4- password successfuly change messgae 
"""