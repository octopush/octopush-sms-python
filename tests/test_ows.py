from __future__ import unicode_literals
import unittest

from octopush import OWS
import octopush

class OWSTest(unittest.TestCase):
    def test_new(self):
        c = OWS('user-login', 'api-key')
        self.assertEqual(c.user_login, 'user-login')
        self.assertEqual(c.api_key, 'api-key')

    def test_should_set_user_login(self):
        c = OWS('user-login', 'api-key')
        self.assertEqual(c.user_login, 'user-login')
        c.set_user_login('ul')
        self.assertEqual(c.user_login, 'ul')

    def test_should_set_api_key(self):
        c = OWS('user-login', 'api-key')
        self.assertEqual(c.api_key, 'api-key')
        c.set_api_key('ak')
        self.assertEqual(c.api_key, 'ak')

    def test_should_set_answer_email(self):
        c = OWS('user-login', 'api-key')
        c.set_answer_email('test')
        self.assertEqual(c.answer_email, 'test')

    def test_should_set_sms_alert_bound(self):
        c = OWS('user-login', 'api-key')
        c.set_sms_alert_bound(100)
        self.assertEqual(c.sms_alert_bound, 100)

    def test_should_set_sms_alert_type(self):
        c = OWS('user-login', 'api-key')
        self.assertEqual(c.sms_alert_type, -1)
        c.set_sms_alert_type(octopush.SMS_PREMIUM)
        self.assertEqual(c.sms_alert_type, octopush.SMS_PREMIUM)