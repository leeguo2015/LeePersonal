# import BaseModel as BaseModel
from django.db import models
# Create your models here.
# Django 未我们提供的ORM框架, 可以更加代码自动生成数据表
# 1.定义模型
# 2.进行数据迁移, 在命令窗口执行
# 2.1 生成迁移文件
# 2.2 执行迁移
from django.contrib.auth.models import AbstractUser

class UserInfo(AbstractUser):
    """用户模型类"""
    nickname = models.CharField(max_length=100, verbose_name="昵称", null=True, default=None, blank=True)
    phone = models.CharField(max_length=16, verbose_name="手机号")
    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

