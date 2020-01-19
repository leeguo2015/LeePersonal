from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def page1_view(request):
    if request.method == 'POST':
        html = "<h1>这是第1个页面post</h1>"
        return HttpResponse(html)
    else:
        # html = "<h1>这是第1个页面get</h1>"
        # return HttpResponse(html)
        return render(request,'boot_.html')


def page1_ex(request):
    if request.method == 'POST':
        html = "<h1>这是第1个页面post</h1>"
        return HttpResponse(html)
    else:
        # html = "<h1>这是第1个页面get</h1>"
        # return HttpResponse(html)
        return render(request,'testHtml.html')