from app import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from app.utils.bootstrap import BootStrapModelForm, BootStrapForm
from app.utils.encrypt import md5
class LoginForm(BootStrapForm):
    name = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )

    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

class TeacherModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.TeacherInfo
        fields = ["name", 'password', "confirm_password","age","gender"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回什么，此字段以后保存到数据库就是什么。
        return confirm
class TeacherEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.TeacherInfo
        fields = ['name']

class TeacherResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.TeacherInfo
        fields = ['password', 'confirm_password']
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)

        # 去数据库校验当前密码和新输入的密码是否一致
        exists = models.TeacherInfo.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError("不能与以前的密码相同")

        return md5_pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回什么，此字段以后保存到数据库就是什么。
        return confirm


class ClassModelForm(BootStrapModelForm):
    class Meta:
        model = models.ClassInfo
        fields = ["title",]
class StudentModelForm(BootStrapModelForm):
    class Meta:
        model = models.StudentInfo
        fields = ["name","gender","depart","math_score","chinese_score","english_score",]
class StudentEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.StudentInfo
        fields = ["math_score","chinese_score","english_score"]