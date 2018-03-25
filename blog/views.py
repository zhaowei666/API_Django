# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import RegistrationSerializer

# Create your views here.

def post_lists(request):

    user = User.objects.filter(username='Jack')
    posts = Post.objects.filter(author=user).order_by('created_time')
    return render(request, 'post_lists.html', {'posts': posts})


@csrf_exempt
def register(request):

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    if not username or not password:
        return HttpResponse(status=400)

    user = User.objects.filter(username=username)
    if user:
        return HttpResponse('User already Registered', status=409)

    user = User.objects.create(username=username)
    user.set_password(password)
    user.save()
    login(request, user)
    return HttpResponse('Account has been created successfully', status=201)


@csrf_exempt
def login_user(request):

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    if not username or not password:
        return HttpResponse(status=400)

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse('logged in successfully', status=200)
    else:
        return HttpResponse('User does not exist or password is incorrect', status=401)


@csrf_exempt
def logout_user(request):
    logout(request)
    return HttpResponse('Logged out successfully', status=200)


