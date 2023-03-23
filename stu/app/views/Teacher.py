# -*- coding=utf-8 -*-
# @Time: 2023/3/22 18:21
# @AUTHOR: HUI
# @File: Teacher.py
# @software: PyCharm
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from app import models
from app.utils.pagination import Pagination
from app.utils.form import TeacherModelForm,TeacherEditModelForm, TeacherResetModelForm


def teacher(request):
    """ 管理员列表 """
    # 构造搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["username__contains"] = search_data

    # 根据搜索条件去数据库获取
    queryset = models.TeacherInfo.objects.filter(**data_dict)
    # 分页
    page_object = Pagination(request, queryset)
    context = {
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
        "search_data": search_data
    }
    return render(request, 'teacher.html', context)

def teacher_edit(request, nid):
    """ 编辑教师 """
    # 对象 / None
    row_object = models.TeacherInfo.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/person/data/')
    title = "编辑"
    if request.method == "GET":
        form = TeacherEditModelForm(instance=row_object)
        return render(request, 'change.html', {"form": form, "title": title})

    form = TeacherEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/person/data/')
    return render(request, 'change.html', {"form": form, "title": title})


def teacher_delete(request, nid):
    """ 删除管理员 """
    models.TeacherInfo.objects.filter(id=nid).delete()
    return redirect('/person/data/')

#
def teacher_reset(request, nid):
    """ 重置密码 """
    # 对象 / None
    row_object = models.TeacherInfo.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/person/data/')

    title = "重置密码 - {}".format(row_object.name)

    if request.method == "GET":
        form = TeacherResetModelForm()
        return render(request, 'change.html', {"form": form, "title": title})

    form = TeacherResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/person/data/')
    return render(request, 'change.html', {"form": form, "title": title})

