import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from app.models import Comments, User


def index(request):
    return HttpResponse('hello world!')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        age = request.POST.get('age')
        try:
            User.objects.get(username=username)
            # return JsonResponse({'code': 1, 'msg': '用户已存在'})
            return HttpResponse('用户已存在！')
        except User.DoesNotExist:
            u = User()
            u.username = username
            u.password = password
            u.age = age
            u.save()
            # return JsonResponse({'code': 0, 'msg': '注册成功'})
            return HttpResponse('注册成功！')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                return HttpResponse('登录成功！')
            else:
                return HttpResponse('用户名或密码不正确！')
        except User.DoesNotExist:
            return HttpResponse('用户名不存在')
    else:
        return render(request, 'login.html')


def xss(request):
    if request.method == 'POST':
        ret = request.POST.get('inp')
        return JsonResponse({'result': ret})
    else:
        return render(request, 'xss.html')


def comments(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        c = Comments()
        if comment:
            c.content = comment
            c.save()
            return JsonResponse({'code': 0, 'msg': '评论成功'})
    else:
        # 方式1：拿到的是一个ValueQuerySet对象 通过values
        res = Comments.objects.values('id', 'content')
        res = json.loads(json.dumps(list(res)))
        return JsonResponse({'code': 0, 'msg': '获取评论列表成功', 'data': res})
