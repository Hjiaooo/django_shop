# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

#前台首页
def index(request):
    return HttpResponse('欢迎进入商城网站前台首页！')