from octopush import SMS
from config import config

sms = SMS(config['user_login'], config['api_key'])
result = sms.credit_sub_account('user@domain.com', 1, 'FR')

print(result)