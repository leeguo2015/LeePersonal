
from django.contrib import admin
from django.urls import path, include
from app_host import views

urlpatterns = [
    path('', views.host),
    # path('boot/container/', views.page2_ex),
    # path('boot/code/', views.boot_code),
    # path('boot/table/', views.boot_table),
    # path('boot/forms/', views.boot_forms),
    # path('boot/button/', views.boot_button),
    # path('boot/drop-down_menu/', views.drop_down_menu),
    # path('boot/buttonGroup/', views.buttonGroup),
    # path('boot/buttonMenu/', views.buttonMenu),

]
