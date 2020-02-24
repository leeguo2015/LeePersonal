from django.db import models

# Create your models here.

# Django 未我们提供的ORM框架, 可以更加代码自动生成数据表
# 1.定义模型
# 2.进行数据迁移, 在命令窗口执行
# 2.1 生成迁移文件
# 2.2 执行迁移

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()