from twilio.rest import Client 
 
def smsMessager(messageBody):
  account_sid = 'ACbc5842ec489c7a7407796bf39f2121e4' 
  auth_token = 'f55be7e0c90e9618b4251b806f77467d' 
  client = Client(account_sid, auth_token) 

  message = client.messages.create( 
    from_='+18434597340',
    body='Automated response from SmartMaintain: {0}'.format(messageBody),         
    to='+18439573064' 
  ) 
  print(message.sid)
