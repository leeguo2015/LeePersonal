
from django.contrib import admin
from django.urls import path, include

from startTest import views

ex_urlpatterns = [
    path('ex/', views.page1_ex),

]
