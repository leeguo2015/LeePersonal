
from django.contrib import admin
from django.urls import path, include

from startTest import views

ex_urlpatterns = [
    path('ex/', views.page1_ex),
    path('boot/container/', views.page2_ex),
    path('boot/code/', views.boot_code),
    path('boot/table/', views.boot_table),
    path('boot/forms/', views.boot_forms),
]
