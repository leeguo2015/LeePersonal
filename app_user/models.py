import BaseModel as BaseModel
from django.db import models
# Create your models here.
# Django 未我们提供的ORM框架, 可以更加代码自动生成数据表
# 1.定义模型
# 2.进行数据迁移, 在命令窗口执行
# 2.1 生成迁移文件
# 2.2 执行迁移
from django.contrib.auth.models import AbstractUser


# class UsersInfo(AbstractUser):
#     # AUTH_USER_MODEL = 'users.User'
#     user_role = models.CharField('角色', max_length=100, blank=True)
#     telephone = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
#     # avatar = models.FileField(verbose_name='头像', upload_to='avatar', default="")

# class User(AbstractUser):
#     """用户模型类"""
#
#     class Meta:
#         db_table = 'df_user'
#         verbose_name = '用户'
#         verbose_name_plural = verbose_name

