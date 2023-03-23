from django.db import models
from datetime import datetime
# Create your models here.
from django.db.models import F
class TeacherInfo(models.Model):
    """ 教师表 """
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    create_time = models.DateField(verbose_name="入职时间", default=datetime.now)
    def __str__(self):
        return self.name
class ClassInfo(models.Model):
    """ 班级表 """
    title = models.CharField(verbose_name='班级', max_length=32)

    def __str__(self):
        return self.title

class StudentInfo(models.Model):
    """ 学生表 """
    name = models.CharField(verbose_name="姓名", max_length=16)
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    depart = models.ForeignKey(verbose_name="班级", to="ClassInfo", to_field="id", on_delete=models.CASCADE)
    math_score = models.IntegerField(verbose_name="数学")
    chinese_score = models.IntegerField(verbose_name="语文")
    english_score = models.IntegerField(verbose_name="英语")
    # ave_score = models.IntegerField(verbose_name="平均成绩", default=0, editable=False)
    # total_score = models.IntegerField(verbose_name="总成绩", default=0, editable=False)
    #
    # def save(self, *args, **kwargs):
    #     self.total_score = F('math_score') + F('english_score') + F('chinese_score')
    #     super(StudentInfo, self).save(*args, **kwargs)
    def total_score(self):
        return (self.math_score + self.english_score + self.chinese_score)
    def ave_score(self):
        return (self.math_score + self.english_score + self.chinese_score) // 3