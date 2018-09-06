# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from common.models import Users
from datetime import datetime

# 浏览会员
def index(request):
    #执行数据查询，并放置到模板中
    list = Users.objects.all()
    context = {"userslist":list}
    #return HttpResponse(list)
    return render(request,'myadmin/users/index.html',context)

# 会员信息添加表单
def add(request):
    return render(request,'myadmin/users/add.html')

#执行会员信息添加
def insert(request):
    try:
        ob = Users()
        ob.username = request.POST['username']
        ob.name = request.POST['name']
        #获取密码并md5
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['password'],encoding="utf8"))
        ob.password = m.hexdigest()
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = 1
        ob.addtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':'添加成功！'}
    except Exception as err:
        print(err)
        context = {'info':'添加失败！'}

    return render(request,"myadmin/info.html",context)

# 执行会员信息删除
def delete(request,uid):
    try:
        ob = Users.objects.get(id=uid)
        ob.delete()
        context = {'info':'删除成功！'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myadmin/info.html",context)

# 打开会员信息编辑表单
def edit(request,uid):
    try:
        ob = Users.objects.get(id=uid)
        context = {'user':ob}
        return render(request,"myadmin/users/edit.html",context)
    except Exception as err:
        print(err)
        context = {'info':'没有找到要修改的信息！'}
    return render(request,"myadmin/info.html",context)

# 执行会员信息编辑
def update(request,uid):
    try:
        ob = Users.objects.get(id=uid)
        ob.name = request.POST['name']
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = request.POST['state']
        ob.save()
        context = {'info':'修改成功！'}
    except Exception as err:
        print(err)
        context = {'info':'修改失败！'}
    return render(request,"myadmin/info.html",context)