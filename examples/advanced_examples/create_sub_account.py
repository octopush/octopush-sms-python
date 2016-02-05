from octopush import SMS
from config import config

sms = SMS(config['user_login'], config['api_key'])
result = sms.create_sub_account('Prenom', 'Nom', 'Raison', 234, 'FR')

print(result)