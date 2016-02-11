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

    def get_credit(self):
        '''
        Returns current user's credit

        :return result dict
        '''
        domain = octopush.DOMAIN
        path = octopush.PATH_CREDIT
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
        if sms_alert_type in [octopush.SMS_PREMIUM, octopush.SMS_WORLD, octopush.SMS_STANDARD]:
            self.sms_alert_type = sms_alert_type