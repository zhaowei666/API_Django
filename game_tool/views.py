# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Room, Player
import random
import json
# Create your views here.


@csrf_exempt
def create_room(request):
    character_dict = json.loads(request.GET.get('characters'))
    characters = []
    for character in character_dict:
        for i in range(character_dict[character]):
            characters.append(character)
    is_new_room = False
    while not is_new_room:
        is_new_room = True
        room_number = str(random.randint(1000, 9999))
        #Room.objects.create(number=room_number, characters=json.dumps(characters), remaining_characters=json.dumps(characters))
        try:
            Room.objects.create(number=room_number, characters=json.dumps(characters), remaining_characters=json.dumps(characters))
        except:
            is_new_room = False
    res = {'room': room_number}
    return JsonResponse(res, status=200)


@csrf_exempt
def draw_character(request):
    player_name = request.GET.get('name')
    room_number = request.GET.get('room')

    rooms = Room.objects.filter(number=room_number)
    if not rooms:
        return HttpResponse('Room Not Found', status='406')
    if len(rooms) > 1:
        return HttpResponse('Room Not Found', status='406')
    room = rooms[0]

    player = Player.objects.filter(name=player_name).first()
    if not player:
        Player.objects.create(name=player_name, room=room)
    else:
        if player.room == room:
            res = {'character': player.character}
            return JsonResponse(res, status=200)

    characters = json.loads(room.characters)
    if not characters:
        return HttpResponse('No characters left', status='406')
    random_int = random.randint(0, len(characters) - 1)
    character = characters[random_int]
    del characters[random_int]

    room.remaining_characters = json.dumps(characters)
    room.save()
    res = {'character': character}
    return JsonResponse(res, status=201)



