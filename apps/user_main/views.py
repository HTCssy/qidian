import json

from django.shortcuts import render,redirect
# Create your views here.
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse

from apps.user_main.models import User
from un1_1 import settings
import django_redis


def error(request):
    return render(request, '../static/home/404-index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            if User.objects.filter(username=username) and User.objects.filter(password=password):
                cache.set(User.u_id, username, settings.REDIS_TIMEOUT)
                return redirect("http://127.0.0.1:8000/static/home/book_first.html")
            else:
                return render(request, 'login.html', {'msg': '账号或者密码不正确'})
        except:
            return redirect('http://127.0.0.1:8000/static/home/404-index.html')
    else:
        return redirect('http://127.0.0.1:8000/static/home/404-index.html')




def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        iphone = request.POST.get('iphone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        if password == re_password:
            try:
                if username and password:
                    user = User.objects.filter(username=username)
                    if not user:
                        User.objects.create(username=username,
                                            password=password,
                                            iphone=iphone,
                                            email=email,
                                            gender=gender,
                                            )
                        cache.set(User.u_id, username, settings.REDIS_TIMEOUT)
                        return render(request, 'success.html')
                        # return HttpResponse(JsonResponse({'session': cache.get('username')}, content_type="application/json"))
                    else:
                        return render(request, 'register.html', {'msg': '用户名已存在'})
                else:
                    return render(request, 'register.html', {'msg': '账户密码不能为空'})
            except Exception as e:
                return redirect('http://127.0.0.1:8000/static/home/404-index.html')
        else:
            return render(request, 'register.html', {'msg': '两次密码输入不一致'})
    else:
        return redirect('http://127.0.0.1:8000/static/home/404-index.html')

def get_session(request):
    session = cache.get(User.u_id)
    if session:
        return HttpResponse(json.dumps({'session': session}), content_type='application/json')

def login_out(request):
    session = cache.set(User.u_id, '登陆', 1*1)
    return redirect('/qidian/login/')