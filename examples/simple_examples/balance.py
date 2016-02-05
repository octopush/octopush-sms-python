from octopush import SMS

sms = SMS('****@***', '**************')

result = sms.get_balance()

for balance in result.findall('balance'):
    print(balance.attrib['type'], balance.text)