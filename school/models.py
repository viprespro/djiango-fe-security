from django.db import models


# Create your models here.
class Teachers(models.Model):
    # 姓名
    name = models.CharField(max_length=20, db_index=True)
    # 生日
    birth = models.DateField()
    # 性别
    gender_choices = [
        (0, '女'),
        (1, '男')
    ]
    gender = models.IntegerField(choices=gender_choices)
    # 是否结婚
    is_married_choices = [
        (0, '未婚'),
        (1, '已婚')
    ]
    is_married = models.IntegerField(choices=is_married_choices)


class Student(models.Model):
    # 姓名
    name = models.CharField(max_length=20)
    # 生日
    birth = models.DateField()
    # 性别
    gender_choices = [
        (0, '女'),
        (1, '男')
    ]
    gender = models.IntegerField(choices=gender_choices)
    # 多对多关联
    teachers = models.ManyToManyField(Teachers)
