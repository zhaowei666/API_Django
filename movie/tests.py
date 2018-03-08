# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import json

# Create your tests here.


class MovieTestCases(TestCase):
    def test_quotes(self):
        response = self.client.get('/movie/quotes?query={}'.format('man'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content)
