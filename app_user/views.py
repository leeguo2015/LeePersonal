import json

from django.shortcuts import render

# Create your views here.
from app_user.models import UserInfo
from django.views.generic import View # 把类作为返回view
from django.db import transaction # 数据库带的回滚操作

def user_info(request):
    pass



class Register(View):
    def get(self, request):
        return render(request, 'userInfo/register.html')

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            password = request.POST.get('password')
            email = request.POST.get('email')
            nickname = request.POST.get('nickname')
            # 此处的User 是 django 自带的model
            # UserInfo.objects.create_user(username=name,
            #                              password=password,
            #                              email=email,
            #                              nickname=nickname,
            #                              )
            # return HttpResponseRedirect('/uauth/dj_login/')
            print("---------------")
            print(request.body)

            receive_data = json.loads(request.body.decode())
            print(name, password, email, nickname)



def logIn(request):
    if request.method == 'GET':
        # do_something()
        return render(request, 'userInfo/logIn.html')
    elif request.method == 'POST':
        # do_something_else()
        pass

def register(request):
    if request.method == 'GET':
        # do_something()
        return render(request, 'userInfo/register.html')
    elif request.method == 'POST':
        if request.method == 'POST':
            name = request.POST.get('name')
            password = request.POST.get('password')
            # 此处的User 是 django 自带的model
            UserInfo.objects.create_user(username=name, password=password)
            # return HttpResponseRedirect('/uauth/dj_login/')


from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

#

@login_required  #没有登录直接访问的话，会根据settings.py中的LOGIN_URL="/login"跳转（有一个默认的）
def crm(request):
    return render(request,"userinfo.html")

def acc_login(request):
    if request.method=="GET":
        return render(request, "login.html")
    if request.method=="POST":
        username=request.POST.get("username")
        print(username)
        password=request.POST.get("password")
        print(password)
        user=authenticate(username=username,password=password)  #只是验证功能，还没有登录
        if user:
            print(user)        #username
            print(type(user))  #<class 'django.contrib.auth.models.User'>
            login(request,user)   #验证通过，登录
            #内部有request.user=user     可以用模板{{request.user}}
            return redirect(request.GET.get("next",'/crm'))    #http://127.0.0.1:8080/login?next=/crm
            #登录成功默认跳转用户信息页面，如果是其他页面来的，登录后跳转到其他页面
        else:
            print(user)        #None
            print(type(user))  #<class 'NoneType'>
            error_msg="用户名或密码错误"
        return render(request, "login.html", {"error_msg":error_msg})
def acc_logout(request):
    logout(request)
    return redirect('/login')
