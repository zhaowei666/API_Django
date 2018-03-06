# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
import datetime
import time
import re

# Create your tests here.

class HelloTestCase(TestCase):
    def test_say_hello(self):
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Hello Tianshu')

    def test_current_time(self):
        response = self.client.get('/hello/time')
        self.assertEqual(response.status_code, 200)
        pattern = 'It is now (\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})'
        re_result = re.findall(pattern, response.content)
        time_list = re_result[0]
        [year, month, day, hour, minute, second] = [int(x) for x in time_list]
        response_ts = float(datetime.datetime(year, month, day, hour, minute, second).strftime('%s'))
        current_ts = time.time()
        self.assertTrue(current_ts - response_ts < 1)


