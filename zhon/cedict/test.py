# -*- coding: utf-8 -*-
"""Tests for the cedict module."""

from __future__ import unicode_literals
import re
import unittest

from zhon import cedict


class TestSimplified(unittest.TestCase):

    simplified_text = '有人丢失了一把斧子怎么找也没有找到'

    def test_re_complement_search(self):
        re_complement = re.compile('[^%s]' % cedict.SIMPLIFIED)
        self.assertEqual(re_complement.search(self.simplified_text), None)


class TestTraditional(unittest.TestCase):

    simplified_text = '有人丢失了一把斧子怎么找也没有找到'

    def test_re_complement_search(self):
        re_complement = re.compile('[^%s]' % cedict.TRADITIONAL)
        self.assertNotEqual(re_complement.search(self.simplified_text), None)
