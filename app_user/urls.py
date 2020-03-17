from django.conf.urls import url, include

from django.urls import path, include
from app_user import views
#应用命名空间,
# 应用明明空间
app_name = "user"  # 防止app重名, 定义应用命名空间

urlpatterns = [
    path('user_info/', views.user_info, name='user_info'),
    path('login/', views.logIn,  name="login"),
    # path('register/', views.register),
    path('register/', views.Register.as_view(), name="register"),
    # 为什么要给url命名, 因为代码种写死了,可能会经常改diamond, 给哥url娶个名字,
    # 以后使用url的时候就能使用塔的名字直接反转了

]
