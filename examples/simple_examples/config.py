import octopush
import datetime

config = {
    'user_login': '******@*****',
    'api_key': '****************',
    'sms_recipients': ['+33600000000'],
    'sms_text': 'test text ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
    'sms_type': octopush.SMS_WORLD,
    'sms_sender': 'onesender'
}