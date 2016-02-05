import octopush
import uuid
from config import config

sms = octopush.SMS(config['user_login'], config['api_key'])
sms.set_sms_text(config['sms_text'])
sms.set_sms_recipients(config['sms_recipients'])
sms.set_sms_type(config['sms_type'])
sms.set_sms_sender(config['sms_sender'])
sms.set_sms_request_id(str(uuid.uuid1()))

result = sms.send()

print(result)