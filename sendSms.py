from twilio.rest import Client 

teslaServiceLink = "https://bit.ly/2qTY540"
bmwServiceLink = "https://bit.ly/2oZwQDg"
audiServiceLink = "https://audi.us/2qRXtvC"
 
def smsMessager(messageBody):
  account_sid = 'ACbc5842ec489c7a7407796bf39f2121e4' 
  auth_token = 'f55be7e0c90e9618b4251b806f77467d' 
  client = Client(account_sid, auth_token) 

  message = client.messages.create( 
    from_='+18434597340',
    body='SmartMaintain: {0}'.format(messageBody),         
    to='+18439573064' 
  ) 
  print(message.sid)
