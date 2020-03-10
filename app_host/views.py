from django.shortcuts import render

# Create your views here.
# from django.template.context_processors import request
# from .models import Question

def host(request):
    return render(request, './hostTemplates/home.html')