# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
# Create your views here.

def say_hello(request):
    return HttpResponse("Hello Tianshu", status=200)


def current_time(request):
    time = datetime.datetime.now()
    html = "<html><body>It is now {}.<body><html>".format(time)
    return HttpResponse(html, status=200)


def offset_time(request, offset):
    try:
        int_offset = int(offset)
    except:
        raise Http404()
    time = datetime.datetime.now() + datetime.timedelta(hours=int_offset)
    html = "<html><body>It is now {} under offset {}<body><html>".format(time, offset)
    return HttpResponse(html, status=200)
