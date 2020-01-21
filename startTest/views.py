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

def page2_ex(request):
    return render(request,'boot_栅格.html')

def boot_code(request):
    return render(request,'boot_code.html')

def boot_table(request):
    return render(request,'boot_table.html')

def boot_forms(request):
    return render(request,'boot_forms.html')
