import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from app.models import Comments


def index(request):
    return HttpResponse('hello world!')


def login(request):
    if request.method == 'POST':
        ret = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        ret['username'] = username
        ret['password'] = password
        ret = json.dumps(ret)
        # return HttpResponse('用户名：' + username + '<br />' + '密码：' + password)
        return HttpResponse(ret, content_type='application/json;charset=utf-8')
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
