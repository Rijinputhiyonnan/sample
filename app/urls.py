"""
URL configuration for cms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views
from .views import *
urlpatterns = [
    path("",views.signin,name="signin"),
    path('dosignin/', views.dosignin, name='dosignin'),
    path('signout/', views.signout, name='signout'),
    
    path("signup",views.signup,name="signup"),
    path("dosignup",views.dosignup,name="dosignup"),
    path('admintable/', views.admintable, name='admintable'),
   
    
    path('addcourse', views.addcourse, name='addcourse'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    
    path('edit_teacher/<int:teacher_id>/', views.edit_teacher, name='edit_teacher'),


    path('delete_teacher/<int:teacher_id>/', delete_teacher, name='delete_teacher'),
    path('edit_admin/<int:teacher_id>/', edit_admin, name='edit_admin'),
    path('delete_admin/<int:teacher_id>/', delete_admin, name='delete_admin'),
    path('teachertable/<int:teacher_id>/', views.teachertable, name='teachertable'),
    path('signup_details/<int:user_id>/', views.signup_details, name='signup_details'),
    path('edit/<int:user_id>/', views.edit, name='edit'),
    path('add_student/', views.add_student, name='add_student'),
    path('student-list/', views.student_list, name='student-list'),
    path('edit-student/<int:student_id>/', views.edit_student, name='edit-student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete-student'),
    path('student-list/', views.student_list, name='student_list'),
    path('student-list2/', views.student_list2, name='student_list2'),
    path('course-table/', views.coursetable, name='coursetable'),
    
]
