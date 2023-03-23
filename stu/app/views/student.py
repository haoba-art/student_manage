# -*- coding=utf-8 -*-
# @Time: 2023/3/23 12:14
# @AUTHOR: HUI
# @File: student.py
# @software: PyCharm
from django.shortcuts import render, redirect
from app import models
from app.utils.pagination import Pagination
from app.utils.form import StudentModelForm,StudentEditModelForm
from django import forms
def student(request):
    """ 学生列表 """

    # 构造搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["name__contains"] = search_data

    # 根据搜索条件去数据库获取
    queryset = models.StudentInfo.objects.filter(**data_dict)
    # 分页
    page_object = Pagination(request, queryset)
    context = {
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
        "search_data": search_data
    }
    return render(request, 'student.html', context)

def student_add(request):

    title = "增加学生"
    if request.method == "GET":
        form = StudentModelForm()
        return render(request, 'change.html', {'form': form, "title": title})
    form = StudentModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/student/')

    return render(request, 'change.html', {'form': form, "title": title})

def student_edit(request, nid):
    """ 编辑学生 """
    # 对象 / None
    row_object = models.StudentInfo.objects.filter(id=nid).first()
    if not row_object:
        # return render(request, 'error.html', {"msg": "数据不存在"})
        return redirect('/student/')

    title = "编辑学生"
    if request.method == "GET":
        form = StudentEditModelForm(instance=row_object)
        return render(request, 'change.html', {"form": form, "title": title})

    form = StudentEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/student/')
    return render(request, 'change.html', {"form": form, "title": title})


def student_delete(request, nid):
    """ 删除管理员 """
    models.StudentInfo.objects.filter(id=nid).delete()
    return redirect('/student/')
