# -*- coding=utf-8 -*-
# @Time: 2023/3/22 19:59
# @AUTHOR: HUI
# @File: account.py
# @software: PyCharm
from app import models
from django.shortcuts import render, HttpResponse, redirect
from app.utils.form import LoginForm,TeacherModelForm
from io import BytesIO
from app.utils.code import check_code
def login(request):
    """ 登录 """
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():

        # 验证码的校验
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'login.html', {'form': form})

        # 去数据库校验用户名和密码是否正确，获取用户对象、None
        Teacher_object = models.TeacherInfo.objects.filter(**form.cleaned_data).first()
        if not Teacher_object:
            form.add_error("password", "用户名或密码错误")
            # form.add_error("username", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})
        # 用户名和密码正确
        # 网站生成随机字符串; 写到用户浏览器的cookie中；在写入到session中；
        request.session["info"] = {'id': Teacher_object.id, 'name': Teacher_object.name}
        # session可以保存7天
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect("/teacher/")

    return render(request, 'login.html', {'form': form})


def image_code(request):
    """ 生成图片验证码 """

    # 调用pillow函数，生成图片
    img, code_string = check_code()
    # 写入到自己的session中（以便于后续获取验证码再进行校验）
    request.session['image_code'] = code_string
    # 给Session设置60s超时
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def logout(request):
    """ 注销 """

    request.session.clear()

    return redirect('/login/')
def register(request):
    """ 注册 """
    title = "教师注册"
    form = TeacherModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/login/')
    return render(request, 'register.html', {'form': form, "title": title})


def person_data(request):
    """个人资料"""
    person = models.TeacherInfo.objects.filter(id=request.session["info"]['id'])
    print(person)
    context = {
        'queryset': person,
    }
    return render(request, 'person_data.html', context)