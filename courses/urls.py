from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
 

urlpatterns = [
    path('', views.home, name='home'),
    path('instructors/' , views.instructors , name= "instructors" ),
    path('allCourses', views.all_Courses, name='allCourses'),
    path('addCourse', views.add_Course, name='addCourse'),
    path('showCourse/<pk>', views.show_Course, name='showCourse'),
    path('course/<pk>/update' , views.update_Course  ,name= "updateCourse"),
    path('course/<pk>/delete' , views.delete_Course  ,name= "deleteCourse"),
    path('lesson/addLesson/<pk>' , views.addLesson ,name= "addLesson"),
    path('lesson/showLesson/<pk>' , views.showLesson ,name= "showLesson"),
    path('lesson/<pk>/update', views.updateLesson, name='updateLesson'),
    path('lesson/<pk>/delete' , views.delete_Lesson ,name= "deleteLesson"),
    path('search/', views.SearchPage, name='search_result'),
    path('courseRegister/<pk>', views.Course_register, name='courseRegister'),
    

     
] + static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)
    

 


