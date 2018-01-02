# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

from .models import Post


def post_lists(request):

    user = User.objects.filter(username='Jack')
    posts = Post.objects.filter(author=user).order_by('created_time')
    return render(request, 'post_lists.html', {'posts': posts})