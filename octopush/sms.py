from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import datetime
import hashlib
import time

import re

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

import requests
from octopush import __version__
import octopush

class SMS:
    def __init__(self, user_login, api_key):
        '''
        Octopush WebService constructor

        :param user_login: Octopush user login
        :param api_key: Octopush API key
        '''
        self.user_login = user_login
        self.api_key = api_key
        self.sms_text = ''
        self.sms_recipients = []
        self.recipients_first_names = []
        self.recipients_last_names = []
        self.sms_fields_1 = []
        self.sms_fields_2 = []
        self.sms_fields_3 = []
        self.sms_mode = octopush.INSTANTANE,
        self.sending_date = int(time.time())
        self.sms_d = datetime.datetime.now().strftime("%d")
        self.sms_m = datetime.datetime.now().strftime("%m")
        self.sms_h = datetime.datetime.now().strftime("%H")
        self.sms_i = datetime.datetime.now().strftime("%M")
        self.sms_y = datetime.datetime.now().strftime("%Y")
        self.sms_sender = 'CampagneSMS'
        self.sms_type = octopush.SMS_STANDARD
        self.request_mode = octopush.REEL
        self.request_id = ''
        self.with_replies = 0
        self.transactional = 0
        self.msisdn_sender = 0
        self.request_keys = ''
        self.user_batch_id = ''
        self.finished = 0

        self._session = requests.Session()
        self._session.headers.update({
            'User-Agent': 'OctopushPy/%s' % __version__,
            'Accept': 'text',
            'Connection': 'close'
        })

    def _request(self, domain, path, port, data):
        response = self._session.post(url=domain + path, data=data)
        if response.status_code >= 200 and response.status_code < 300:
            try:
                doc = ET.fromstring(response.content)
            except Exception as e:
                raise Exception(e)

            if doc.find('error_code').text == '000':
                return doc
            else:
                raise Exception(octopush.ERRORS[doc.find('error_code').text])
        else:
            raise Exception(response.content)

    def send(self):
        '''
        Sends SMS message

        :return: result dict
        '''
        domain = octopush.DOMAIN
        path = octopush.PATH_SMS
        port = octopush.PORT

        data = {
            'user_login': self.user_login,
            'api_key': self.api_key,
            'sms_text': self.sms_text,
            'sms_recipients': ','.join(self.sms_recipients),
            'recipients_first_names': ','.join(self.recipients_first_names),
            'recipients_last_names': ','.join(self.recipients_last_names),
            'sms_fields_1': ','.join(self.sms_fields_1),
            'sms_fields_2': ','.join(self.sms_fields_2),
            'sms_fields_3': ','.join(self.sms_fields_3),
            'sms_mode': self.sms_mode,
            'sms_type': self.sms_type,
            'sms_sender': self.sms_sender,
            'request_mode': self.request_mode,
            'request_id': self.request_id,
            'with_replies': self.with_replies,
            'transactional': self.transactional,
            'msisdn_sender': self.msisdn_sender,
        }

        if self.sms_mode == octopush.DIFFERE:
            data['sending_date'] = self.sending_date

        if self.request_keys != '':
            data['request_keys'] = self.request_keys
            data['request_sha1'] = self._get_request_sha1_string(self.request_keys, data)

        return self._request(domain, path, port, data)

    def create_sub_account(self, first_name, last_name, raison_sociale, alert_bound, alert_sms_type):
        '''
        Creates sub account
        :param first_name:  first name
        :param last_name:   last name
        :param raison_sociale:  raison sociale
        :param alert_bound: alert bound
        :param alert_sms_type:  octopush.SMS_STANDARD, octopush.SMS_WORLD, octopush.SMS_PREMIUM
        :return:
        '''
        domain = octopush.DOMAIN
        path = octopush.PATH_SUB_ACCOUNT
        port = octopush.PORT

        data = {
            'user_login': self.user_login,
            'api_key': self.api_key,
            'first_name': first_name,
            'last_name': last_name,
            'raison_sociale': raison_sociale,
            'alert_bound': alert_bound,
            'alert_sms_type': alert_sms_type
        }

        return self._request(domain, path, port, data)

    def credit_sub_account(self, sub_account_email, sms_amount, sms_type):
        '''
        Credits sub account

        :param sub_account_email: subaccount email
        :param sms_amount: number of credits
        :param sms_type: octopush.SMS_STANDARD, octopush.SMS_WORLD, octopush.SMS_PREMIUM
        :return result dict
        '''

        domain = octopush.DOMAIN
        path = octopush.PATH_CREDIT_SUB_ACCOUNT_TOKEN
        port = octopush.PORT

        data = {
            'user_login': self.user_login,
            'api_key': self.api_key,
            'sub_account_email': sub_account_email
        }

        result = self._request(domain, path, port, data)

        token = result['octopush']['token']
        if sms_type != 'FR' and sms_type != 'XXX':
            sms_type = 'FR'

        data = {
            'user_login': self.user_login,
            'api_key': self.api_key,
            'sub_account_email': sub_account_email,
            'sms_number': sms_amount,
            'sms_type': sms_type,
            'token': token
        }

        return self._request(domain, path, port, data)

    def get_balance(self):
        '''
        Returns current user's balance

        :return result dict
        '''
        domain = octopush.DOMAIN
        path = octopush.PATH_BALANCE
        port = octopush.PORT

        data = {
            'user_login': self.user_login,
            'api_key': self.api_key,
        }

        return self._request(domain, path, port, data)

    def _get_request_sha1_string(self, request_keys, data):
        A_char_to_field = {
            'T': 'sms_text',
            'R': 'sms_recipients',
            'M': 'sms_mode',
            'Y': 'sms_type',
            'S': 'sms_sender',
            'D': 'sms_date',
            'a': 'recipients_first_names',
            'b': 'recipients_last_names',
            'c': 'sms_fields_1',
            'd': 'sms_fields_2',
            'e': 'sms_fields_3',
            'W': 'with_replies',
            'N': 'transactional',
            'Q': 'request_id'
        }
        request_string = ''
        for char in request_keys:
            if char in A_char_to_field and A_char_to_field[char] in data:
                request_string += data[A_char_to_field[char]]
        return hashlib.sha1(request_string.encode('utf-8')).hexdigest()

    def set_user_login(self, user_login):
        '''
        Sets Octopush API user login

        :param user_login: user_login
        '''
        self.user_login = user_login

    def set_api_key(self, api_key):
        '''
        Sets Octopush API key

        :param api_key: api_key
        '''
        self.api_key = api_key

    def set_sms_text(self, value):
        '''
        Sets sms_text
        :param value: value
        '''
        self.sms_text = value

    def set_sms_type(self, value):
        '''
        Sets sms_type
        :param value: value
        '''
        self.sms_type = value

    def set_sms_recipients(self, value):
        '''
        Sets sms_recipients list
        :param value: value
        '''
        self.sms_recipients = value

    def set_recipients_first_names(self, value):
        '''
        Sets recipients_first_names list
        :param value: value
        '''
        self.recipients_first_names = value

    def set_recipients_last_names(self, value):
        '''
        Sets recipients_last_names list
        :param value: value
        '''
        self.recipients_last_names = value

    def set_sms_fields_1(self, value):
        '''
        Sets sms_fields_1 list
        :param value: value
        '''
        self.sms_fields_1 = value

    def set_sms_fields_2(self, value):
        '''
        Sets sms_fields_2 list
        :param value: value
        '''
        self.sms_fields_2 = value

    def set_sms_fields_3(self, value):
        '''
        Sets sms_fields_3 list
        :param value: value
        '''
        self.sms_fields_3 = value

    def set_sms_mode(self, value):
        '''
        Sets sms_mode
        :param value: octopush.INSTANTANE or octopush.DIFFERE
        '''
        self.sms_mode= value

    def set_sms_sender(self, value):
        '''
        Sets sms_sender
        :param value: string
        '''
        self.sms_sender = value

    def set_date(self, y, m, d, h, i):
        '''
        Sets date when SMS should be send in case if sms_mode = DIFFERE

        :param y: year
        :param m: month
        :param d: day
        :param h: hour
        :param i: minutes
        '''
        self.sms_y = y
        self.sms_m = m
        self.sms_d = d
        self.sms_h = h
        self.sms_i = i

        self.sending_date = int(time.mktime(datetime.datetime(y, m, d, h, i).timetuple()))

    def set_simulation_mode(self):
        '''
        Sets request_mode to simulation state
        '''
        self.request_mode = octopush.SIMULATION

    def set_sms_ticket(self, value):
        '''
        Sets sms_ticket
        :param value: value
        '''
        self.sms_ticket = value

    def set_sms_request_id(self, value):
        '''
        Sets unique SMS request ID
        :param value: value
        '''
        self.request_id = re.compile(r'[^0-9a-zA-Z]+').sub('', value)

    def set_option_with_replies(self, value):
        '''
        Notify Octopush platform that you want to receive the answers that your recipients will send back to your sending(s)
        :param value: value
        '''
        self.with_replies = value

    def set_option_transactional(self, value):
        '''
        Notify Octopush that you are making a transactional sending.
        With this option, sending marketing SMS is strongly forbidden, and may make your account blocked in case of abuses.
        DO NOT USE this option if you are not sure to understand what a transactional SMS is.
        :param value: value
        '''
        self.transactional = value

    def set_sender_is_msisdn(self, value):
        '''
        Use a MSISDN number
        :param value: value
        '''
        self.msisdn_sender = value

    def set_request_keys(self, value):
        '''
        Lists the key fields of the application you want to add in the sha1 hash. Example: 'TRYS ' (for fields sms_text, sms_recipients, sms_type, sms_sender).
        :param value: value
        '''
        self.request_keys = value

    def set_user_batch_id(self, value):
        '''
        :param value: value
        '''
        self.user_batch_id = re.compile(r'[^0-9a-zA-Z]+').sub('', value)

    def set_finished(self, value):
        '''
        Sets
        :param value: value
        '''
        self.finished = value

    def set_action(self, value):
        '''
        Sets
        :param value: value
        '''
        self.action = value