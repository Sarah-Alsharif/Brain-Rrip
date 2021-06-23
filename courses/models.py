from django.db import models
from django.contrib.auth.models import User 
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
import django_better_admin_arrayfield.models.fields
from django.forms import ModelForm
 

class Courses(models.Model):
    name = models.CharField( max_length=50)
    description = models.CharField(max_length=500)
    photo_url = models.CharField(max_length=500)
    no_lessons = models.IntegerField(null = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    registerd_users = models.ManyToManyField(User, related_name='mycourses' , blank = True)
    
    def __str__(self):
        return self.name


class Lessons(models.Model):
    title = models.CharField( max_length=50)
    description = models.CharField( max_length=500)
    duration = models.IntegerField(null = True)
    video = models.CharField( max_length=500)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return '%s %s' %(self.title, self.course.id)