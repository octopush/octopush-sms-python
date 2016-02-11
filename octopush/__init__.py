#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A library provides Python interface to the Octopush API"""
from __future__ import absolute_import

__author__ = 'Octopush'
__version__ = '1.0.0'

from .sms import SMS
from .ows import OWS

VERSION = '1.0.0'
DOMAIN = 'http://www.octopush-dm.com'
PORT = 80
PATH = ''
PATH_BIS = ''
PATH_SMS = PATH + '/api/sms'
PATH_CREDIT = PATH + '/api/credit'
_CUT_ = 7
SMS_STANDARD = 'XXX'
SMS_WORLD = 'WWW'
SMS_PREMIUM = 'FR'
SIMULATION = 'simu'
REEL = 'real'
ERRORS = {
    '100': 'POST request missing.',
    '101': 'Incorrect login details.',
    '102': 'Your SMS exceeds 160 characters',
    '103': 'Your message has no recipients',
    '104': 'You have run out of credit.',
    '105': 'You don\'t have enough credit on your balance, but your last order is waiting for being validated',
    '106': 'You have entered the Sender incorrectly. 3 to 11 characters, chosen from 0 to 9, a to z, A to Z. No accent, space or punctuation.',
    '107': 'The text of your message is missing.',
    '108': 'You have not entered your login details.',
    '109': 'You have not entered your password.',
    '110': 'You have not entered the list of recipient.',
    '111': 'You have not chosen a way to enter your recipients.',
    '112': 'You have not defined the quality of your message.',
    '113': 'Your account is not validated. Log in Octopush and go to the "User interface" section.',
    '114': 'You are under investigation for the fraudulent use of our services.',
    '115': 'The recipient number is different from the number of one of the parameters that you have related it to.',
    '116': 'The mailing option only works by using a contact list.',
    '117': 'Your recipient list contains no correct numbers. Have you formatted your numbers by including the international dialling code? Contact us if you have any problems.',
    '118': 'You must tick one of the two boxes to indicate if you do not wish to send test SMS or if you have correctly received and validated it.',
    '119': 'You cannot send SMS with more than 160 characters for this type of SMS',
    '120': 'A SMS with the same request_id has already been sent.',
    '121': 'In Premium SMS, the mention "STOP au XXXXX" is mandatory and must belong to your text (respect the case).',
    '122': 'In Standard SMS, the mention "no PUB=STOP" is mandatory and must belong to your text (respect the case).',
    '123': 'The field request_sha1 is missing.',
    '124': 'The field request_sha1 does not match. The data is wrong, or the query string contains an error or the frame contains an error : the request is rejected.',
    '125': 'An undefined error has occurred. Please contact support.',
    '126': 'An SMS campaign is already waiting for approval to send. You must validate or cancel it in order to start another.',
    '127': 'An SMS campaign is already being processed. You must wait for processing to be completed in order to start another.',
    '128': 'Too many attempts have been made. You need to start a new campaign.',
    '129': 'Campaign is being built.',
    '130': 'Campagne has not been set as finished.',
    '131': 'Campaign not found.',
    '132': 'Campaign sent.',
    '133': 'The user_batch_id has already been used',
    '150': 'No country was found for this prefix.',
    '151': 'The recipient country is not part of the countries serviced by Octopush.',
    '152': 'You cannot send low cost SMS to this country. Choose Premium SMS',
    '153': 'The route is congested. This type of SMS cannot be dispatched immediately. If your order is urgent, please use another type of SMS.',
    '201': 'This option is only available on request. Do not hesitate to request access if you need it.',
    '202': 'The email account you wish to credit is incorrect.',
    '203': 'You already have tokens in use. You can only have one session open at a time.',
    '204': 'You specified a wrong token.',
    '205': 'The number of text messages you want to transfer is too low.',
    '206': 'You may not run campaigns during a credit transfer.',
    '207': 'You do not have access to this feature.',
    '208': 'Wrong type of SMS.',
    '209': 'You are not allowed to send SMS messages to this user.',
    '210': 'This email is not specified in any of your sub accounts or affiliate users.',
    '300': 'You are not authorized to manage your lists by API.',
    '301': 'You have reached the maximum number of lists.',
    '302': 'A list with the same name already exists.',
    '303': 'The specified list does not exist.',
    '304': 'The list is already full.',
    '305': 'There are too many contacts in the query.',
    '306': 'The requested action is unknown.',
    '308': 'Error of file.',
    '500': 'Impossible to process the requested action',
    '501': 'Connection error. Please contact our customer support'
}


def etree_to_dict(element):
    node = dict()

    text = getattr(element, 'text', None)
    if text is not None:
        node['text'] = text

    node.update(element.items()) # element's attributes

    child_nodes = {}
    for child in element: # element's children
        child_nodes.setdefault(child, []).append( etree_to_dict(child) )

    # convert all single-element lists into non-lists
    for key, value in child_nodes.items():
        if len(value) == 1:
            child_nodes[key] = value[0]

    node.update(child_nodes.items())

    return node