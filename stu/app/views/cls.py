# -*- coding=utf-8 -*-
# @Time: 2023/3/23 10:48
# @AUTHOR: HUI
# @File: cls.py
# @software: PyCharm
from django.shortcuts import render, redirect
from app import models
from app.utils.pagination import Pagination
from app.utils.form import ClassModelForm
def class_list(request):
    """ 班级列表 """

    # 构造搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["title__contains"] = search_data

    # 根据搜索条件去数据库获取
    queryset = models.ClassInfo.objects.filter(**data_dict)
    # 分页
    page_object = Pagination(request, queryset)
    context = {
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
        "search_data": search_data
    }
    return render(request, 'class_list.html', context)


def class_add(request):
    """ 添加班级 """
    title = "新建班级"
    if request.method == "GET":
        form = ClassModelForm()
        return render(request, 'change.html', {'form': form, "title": title})
    form = ClassModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/class/list/')
    return render(request, 'change.html', {'form': form, "title": title})
def class_edit(request, nid):
    row_object = models.ClassInfo.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/class/list/')
    title = "编辑"
    if request.method == "GET":
        form = ClassModelForm(instance=row_object)
        return render(request, 'change.html', {"form": form, "title": title})
    form = ClassModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/class/list/')
    return render(request, 'change.html', {"form": form, "title": title})
def class_delete(request, nid):
    """ 删除班级 """
    models.ClassInfo.objects.filter(id=nid).delete()
    return redirect('/class/list/')