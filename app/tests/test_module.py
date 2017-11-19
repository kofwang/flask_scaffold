#!/usr/bin/env python
#-*- coding: utf-8 -*-
import unittest
from app.models.demo import Demo

class TestDemo(unittest.TestCase):

    def setUp(self):
        self.val = 1

    def tearDown(self):
        pass

    def test_demo(self):
        self.assertEqual(Demo.sayhi(), 'hello world')
        self.assertEqual(self.val, 1)

if __name__ == '__main__':
    unittest.main()
