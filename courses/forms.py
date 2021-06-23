from django.forms import ModelForm , Textarea
from .models import Courses, Lessons
from django import forms

class CourseForm(ModelForm):
    
    class Meta:
        model = Courses
        fields = ("name" , "description" , "photo_url" , "no_lessons")
        exclude=['owner']

class LessonForm(ModelForm):
    
    class Meta:
        model = Lessons
        fields = ("title" ,"description" , "duration" , "video")
        exclude=['course']
       
         




