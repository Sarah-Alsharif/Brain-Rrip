from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Courses, Lessons 
from .forms import CourseForm, LessonForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):

    return render(request, 'home.html', {})

# all courses


def all_Courses(request):

    all_Courses = Courses.objects.all()
    return render(request, 'courses/all_courses.html',
                  {"all_Courses": all_Courses})

# add new course


def add_Course(request):
    owner_name = User.objects.get(id=request.user.id)
    print(owner_name)
    temp = Courses( owner=owner_name)
    form = CourseForm()
    print(request.method)
    if (request.method == "POST"):
        course = CourseForm(request.POST, instance=temp)
        if (course.is_valid()):
            course.save()
            messages.add_message(request, messages.SUCCESS, "Course added successfully!")
            return redirect('allCourses')

    return render(request, 'courses/addcourse.html',
                  {'form': form}
                  )

# show one course


def show_Course(request, pk):
    id_ = pk
    try:
        one_course = Courses.objects.get(id=pk)
    except Exception:
        return HttpResponse("error")

    return render(request, 'courses/show_course.html',
                  {"one_course": one_course
                   })



# update course
def update_Course(request, pk):
    update_course = Courses.objects.get(pk=pk)
    form = CourseForm(instance=update_course)
    if (request.method == "POST"):
        Updated_course = CourseForm(request.POST, instance=update_course)
        if Updated_course.is_valid():
            Updated_course.save()
            messages.add_message(request, messages.SUCCESS, "Course updated successfully!")
            return redirect(f'/showCourse/{pk}')
    return render(request, 'courses/addcourse.html', {"form": form})


def instructors(request):

    all_instructors = User.objects.all()
    return render(request, 'instructor/instructors.html' , {"all_instructors" : all_instructors})



# add delete course
def delete_Course(request, pk):
    course = Courses.objects.get(pk=pk)
    course.delete()
    messages.add_message(request, messages.SUCCESS, "Course deleted successfully!")
    return redirect('/mycourses')


# add a new lesson
def addLesson(request, pk):
    form = LessonForm()
    print(request.method)
    if (request.method == "POST"):
        currint_course = Courses.objects.get(pk=pk)
        temp = Lessons(course=currint_course)
        lesson = LessonForm(request.POST,instance=temp)
        if (lesson.is_valid()):
            lesson.save()
            messages.add_message(request, messages.SUCCESS, "Lesson added successfully!")
            return redirect(f'/showCourse/{pk}')

    return render(request, 'lesson/addLesson.html',
                  {'form': form})
    
# update lesson
def updateLesson(request, pk):
    update_lesson = Lessons.objects.get(pk=pk)
    form = LessonForm(instance=update_lesson)
    if (request.method == "POST"):
        Updated_lesson = LessonForm(request.POST, instance=update_lesson)
        if Updated_lesson.is_valid():
            Updated_lesson.save()
            messages.add_message(request, messages.SUCCESS, "Lesson updated successfully!")
            return redirect(f'/lesson/showLesson/{pk}')
    return render(request, 'lesson/addLesson.html', {"form": form})

# Search Bar
def SearchPage(request):
    srh = request.GET['query']
    courses = Courses.objects.filter(name__icontains=srh)
    if(not courses):
        messages.add_message(request, messages.WARNING, "Course not found.")
        return render(request, 'courses/all_courses.html')
    else:
        params = {'courses': courses, 'search': srh}
        return render(request, 'courses/all_courses.html', params)


def showLesson(request, pk):
    id_ = pk
    try:
        one_lesson = Lessons.objects.get(id=pk)
    except Exception:
        return HttpResponse("error")

    return render(request, 'lesson/showLesson.html',
                  {"one_lesson": one_lesson
                   })

# add delete course
def delete_Lesson(request, pk):
    lesson = Lessons.objects.get(pk=pk)
    print(lesson.course.id)
    print(type(lesson))
    course_pk = lesson.course.id 
    lesson.delete()
    messages.add_message(request, messages.SUCCESS, "Lesson deleted successfully!")
    return redirect(f'/showCourse/{course_pk}')


# register course
@login_required()
def Course_register(request, pk):
    user = User.objects.get(pk=request.user.id)
    course = Courses.objects.get(pk=pk)
    if not user in course.registerd_users.all():
        course.registerd_users.add(user)
        messages.add_message(request, messages.SUCCESS,
                             "You have successfully registerd in this course!")

    print(course.registerd_users.all())
    return redirect(f'/showCourse/{pk}')


