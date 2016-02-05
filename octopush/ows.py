from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

import requests
from octopush import __version__
import octopush

class OWS:
    def __init__(self, user_login, api_key):
        '''
        Octopush WebService constructor

        :param user_login: Octopush user login
        :param api_key: Octopush API key
        '''
        self.user_login = user_login
        self.api_key = api_key
        self.answer_email = -1
        self.sms_alert_bound = -1
        self.sms_alert_type = -1

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

    def edit_options(self):
        '''
        Updates options on server
        :return result dict
        '''
        domain = octopush.DOMAIN
        path = octopush.PATH_EDIT_OPTIONS
        port = octopush.PORT

        data = {
            'user_login': self.user_login,
            'api_key': self.api_key,
        }

        if self.answer_email != -1:
            data['answer_email'] = self.answer_email

        if self.sms_alert_bound != -1:
            data['sms_alert_bound'] = self.sms_alert_bound

        if self.sms_alert_type != -1:
            data['sms_alert_type'] = self.sms_alert_type

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

    def set_answer_email(self, answer_email):
        '''
        Sets answer email

        :param answer_email: answer_email
        '''
        self.answer_email = answer_email

    def set_sms_alert_bound(self, sms_alert_bound):
        '''
        Sets SMS alert bound

        :param sms_alert_bound: SMS alert bound
        '''
        self.sms_alert_bound = int(sms_alert_bound)

    def set_sms_alert_type(self, sms_alert_type):
        '''
        Sets SMS alert type

        :param sms_alert_type: SMS alert type
        '''
        if sms_alert_type in [octopush.SMS_PREMIUM, octopush.SMS_STANDARD]:
            self.sms_alert_type = sms_alert_type