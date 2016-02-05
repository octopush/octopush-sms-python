# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

import os

from octopush import SMS

class NetTest(unittest.TestCase):
    def test_get_balance(self):
        if os.environ.get('OCTOPUSH_USER_LOGIN') is not None and os.environ.get('OCTOPUSH_API_KEY') is not None:
            c = SMS(os.environ.get('OCTOPUSH_USER_LOGIN'), os.environ.get('OCTOPUSH_API_KEY'))
            r = c.get_balance()

            self.assertGreater(len(r.findall('balance')), 1)