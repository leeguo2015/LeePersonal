from django.shortcuts import render

# Create your views here.
# from django.template.context_processors import request
# from .models import Question
from django.views.generic import View


class Host(View):
    def get(self, request):
        return render(request, 'app_host/home.html')

def host(request):
    return render(request, 'app_host/home.html')