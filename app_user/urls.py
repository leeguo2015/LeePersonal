
from django.conf.urls import url, include

from django.urls import path, include
from app_user import views

urlpatterns = [
    path('user_info', views.user_info),
]
