"""stu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from app.views import Teacher,account,cls,student
urlpatterns = [
    # 教师
    path('',Teacher.teacher),
    path('teacher/',Teacher.teacher),
    path('teacher/<int:nid>/edit/', Teacher.teacher_edit),
    path('teacher/<int:nid>/delete/', Teacher.teacher_delete),
    path('teacher/<int:nid>/reset/', Teacher.teacher_reset),
# 班级
    path('class/list/',cls.class_list),
    path('class/add/',cls.class_add),
    path('class/<int:nid>/edit/', cls.class_edit),
    path('class/<int:nid>/delete/', cls.class_delete),
# 学生
    path('student/',student.student),
    path('student/add/',student.student_add),
    path('student/<int:nid>/edit/', student.student_edit),
    path('student/<int:nid>/delete/', student.student_delete),
# 登录
    path('login/',account.login),
    path('logout/',account.logout),
    path('register/',account.register),
    path('image/code/', account.image_code),
    path('person/data/',account.person_data),
]
