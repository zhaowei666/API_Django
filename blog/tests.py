# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.


class UserTestCases(TestCase):

    user1 = {'username': 'user1', 'password': '123456'}
    user2 = {'username': 'user2', 'password': '123456'}
    user3 = {'username': 'user3', 'password': '123456'}
    user3_2 = {'username': 'user3', 'password': 'abcdefg'}
    user3 = {'username': 'user4', 'password': '123456'}

    def test_register(self):
        response = self.client.post('/register', self.user1)
        self.assertEqual(response.status_code, 201)

    def test_login_logout(self):
        response = self.client.post('/register', self.user2)
        self.assertEqual(response.status_code, 201)

        response = self.client.post('/logout')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/login', self.user2)
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/login', self.user3)
        self.assertEqual(response.status_code, 401)

        response = self.client.post('/login', self.user3_2)
        self.assertEqual(response.status_code, 401)

