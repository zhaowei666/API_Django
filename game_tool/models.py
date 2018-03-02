# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models


class Room(models.Model):
    number = models.CharField(max_length=4, primary_key=True)
    characters = models.CharField(max_length=200, null=False)
    judge = models.BooleanField(default=False)
    remaining_characters = models.CharField(max_length=200)


class Player(models.Model):
    name = models.CharField(unique=True, max_length=20)
    room = models.ForeignKey(Room)
    character = models.CharField(max_length=30)
