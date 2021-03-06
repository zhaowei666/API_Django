# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.created_time = timezone.now()
        self.save()

    def __str__(self):
        return self.title