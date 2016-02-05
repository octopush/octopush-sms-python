from octopush import SMS
from config import config

sms = SMS(config['user_login'], config['api_key'])

result = sms.get_balance()

for balance in result.findall('balance'):
    print(balance.attrib['type'], balance.text)