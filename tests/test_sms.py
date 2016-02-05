# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

import time

import datetime

from octopush import SMS
import octopush

class SMSTest(unittest.TestCase):
    def test_new(self):
        c = SMS('user-login', 'api-key')
        self.assertEqual(c.user_login, 'user-login')
        self.assertEqual(c.api_key, 'api-key')

    def test_should_set_user_login(self):
        c = SMS('user-login', 'api-key')
        self.assertEqual(c.user_login, 'user-login')
        c.set_user_login('ul')
        self.assertEqual(c.user_login, 'ul')

    def test_should_set_api_key(self):
        c = SMS('user-login', 'api-key')
        self.assertEqual(c.api_key, 'api-key')
        c.set_api_key('ak')
        self.assertEqual(c.api_key, 'ak')

    def test_should_set_sms_text(self):
        c = SMS('user-login', 'api-key')
        c.set_sms_text('test')
        self.assertEqual(c.sms_text, 'test')

    def test_should_set_sms_type(self):
        c = SMS('user-login', 'api-key')
        c.set_sms_type('test')
        self.assertEqual(c.sms_type, 'test')

    def test_should_set_sms_recipients(self):
        c = SMS('user-login', 'api-key')
        c.set_sms_recipients('test')
        self.assertEqual(c.sms_recipients, 'test')

    def test_should_set_recipients_first_names(self):
        c = SMS('user-login', 'api-key')
        c.set_recipients_first_names('test')
        self.assertEqual(c.recipients_first_names, 'test')

    def test_should_set_recipients_last_names(self):
        c = SMS('user-login', 'api-key')
        c.set_recipients_last_names('test')
        self.assertEqual(c.recipients_last_names, 'test')

    def test_should_set_sms_fields_1(self):
        c = SMS('user-login', 'api-key')
        c.set_sms_fields_1('test')
        self.assertEqual(c.sms_fields_1, 'test')

    def test_should_set_sms_fields_2(self):
        c = SMS('user-login', 'api-key')
        c.set_sms_fields_2('test')
        self.assertEqual(c.sms_fields_2, 'test')

    def test_should_set_sms_fields_3(self):
        c = SMS('user-login', 'api-key')
        c.set_sms_fields_3('test')
        self.assertEqual(c.sms_fields_3, 'test')

    def test_should_set_sms_mode(self):
        c = SMS('user-login', 'api-key')
        c.set_sms_mode(octopush.DIFFERE)
        self.assertEqual(c.sms_mode, octopush.DIFFERE)

    def test_should_set_sms_sender(self):
        c = SMS('user-login', 'api-key')
        c.set_sms_sender('test')
        self.assertEqual(c.sms_sender, 'test')

    def test_should_set_sms_date(self):
        c = SMS('user-login', 'api-key')
        c.set_date(2000, 1, 1, 0, 0)
        self.assertEqual(c.sending_date, int(time.mktime(datetime.datetime(2000, 1, 1, 0, 0).timetuple())))

    def test_should_set_request_mode(self):
        c = SMS('user-login', 'api-key')
        self.assertEqual(c.request_mode, octopush.REEL)
        c.set_simulation_mode()
        self.assertEqual(c.request_mode, octopush.SIMULATION)

    def test_should_set_sms_ticket(self):
        c = SMS('user-login', 'api-key')
        c.set_sms_ticket('test')
        self.assertEqual(c.sms_ticket, 'test')

    def test_should_set_request_id(self):
        c = SMS('user-login', 'api-key')
        c.set_sms_request_id('12abcdefgh34!.')
        self.assertEqual(c.request_id, '12abcdefgh34')

    def test_should_set_with_replies(self):
        c = SMS('user-login', 'api-key')
        c.set_option_with_replies(1)
        self.assertEqual(c.with_replies, 1)

    def test_should_set_transactional(self):
        c = SMS('user-login', 'api-key')
        c.set_option_transactional(1)
        self.assertEqual(c.transactional, 1)

    def test_should_set_msisdn_sender(self):
        c = SMS('user-login', 'api-key')
        c.set_sender_is_msisdn('test')
        self.assertEqual(c.msisdn_sender, 'test')

    def test_should_set_request_keys(self):
        c = SMS('user-login', 'api-key')
        c.set_request_keys('test')
        self.assertEqual(c.request_keys, 'test')

    def test_should_set_user_batch_id(self):
        c = SMS('user-login', 'api-key')
        c.set_user_batch_id('12abcdefgh34!.')
        self.assertEqual(c.user_batch_id, '12abcdefgh34')

    def test_should_set_finished(self):
        c = SMS('user-login', 'api-key')
        c.set_finished('test')
        self.assertEqual(c.finished, 'test')

    def test_should_set_action(self):
        c = SMS('user-login', 'api-key')
        c.set_action('test')
        self.assertEqual(c.action, 'test')

    def test_utf8_sha1(self):
        c = SMS('user-login', 'api-key')
        c.set_sms_text(u'àбрвалг')
        c.set_request_keys('T')
        h = c._get_request_sha1_string('T', {
            'sms_text': u'àбрвалг'
        })
        self.assertEqual(h, 'c611522535baf80debd3f24bafa434d14fb21d9d')
