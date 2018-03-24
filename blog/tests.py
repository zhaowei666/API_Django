# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.


class UserTestCases(TestCase):

    user1 = {'username': 'user1', 'password': '123456'}

    def test_register(self):
        response = self.client.post('/register', self.user1)
        print('~~~~~~~')
        print(response.content)
        print('@@@@@@@2')
        self.assertEqual(response.status_code, 201)
