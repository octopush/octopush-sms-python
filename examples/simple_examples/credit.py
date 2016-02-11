from octopush import SMS
from config import config

sms = SMS(config['user_login'], config['api_key'])

result = sms.get_credit()

for credit in result.findall('credit'):
    print(credit.text)