from django.shortcuts import render

# Create your views here.
# from django.template.context_processors import request
# from .models import Question

def host(request):
    # print("aaaaaaaaaaaaaaaaaaaaaaaa")
    return render(request, 'host.html')