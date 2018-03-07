# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import json

# Create your tests here.


class GameToolTestCases(TestCase):
    def test_create_room(self):
        characters = {
            'seer': 1,
            'witch': 1
        }
        response = self.client.get('/game_tool/create_room?characters={}'.format(json.dumps(characters)))
        print '***********~~~~~~~~~~~~'
        print response.content
        print '@@@@@@@@@@'
        room_number = json.loads(response.content)['room']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(room_number), 4)
        self.assertTrue(room_number.isdigit())

    def test_draw_character(self):

        # create room
        characters = {
            'seer': 1,
            'witch': 1
        }
        response = self.client.get('/game_tool/create_room?characters={}'.format(json.dumps(characters)))
        room_number = json.loads(response.content)['room']

        # draw first card
        response = self.client.get('/game_tool/draw_character?name={}&room={}'.format('p1', str(room_number)))
        self.assertEqual(response.status_code, 201)
        card1 = json.loads(response.content)['character']
        self.assertTrue(card1 in characters)

        # draw second card
        response = self.client.get('/game_tool/draw_character?name={}&room={}'.format('p2', str(room_number)))
        self.assertEqual(response.status_code, 201)
        card2 = json.loads(response.content)['character']
        self.assertTrue(card2 in characters and card2 != card1)

        # try to draw a third card which is not in the pool
        response = self.client.get('/game_tool/draw_character?name={}&room={}'.format('p3', str(room_number)))
        self.assertEqual(response.status_code, 202)
        error = json.loads(response.content)['error']
        self.assertEqual(error, 'No cards left in the pool')

        # check a card that has been drawn before
        response = self.client.get('/game_tool/draw_character?name={}&room={}'.format('p2', str(room_number)))
        self.assertEqual(response.status_code, 200)






