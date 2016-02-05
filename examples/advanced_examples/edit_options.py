from octopush import OWS
from config import config
import octopush

ows = OWS(config['user_login'], config['api_key'])
ows.set_sms_alert_bound(100)
ows.set_sms_alert_type(octopush.SMS_STANDARD)
result = ows.edit_options()

print(result)