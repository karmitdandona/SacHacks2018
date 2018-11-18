from twilio.rest import Client 

teslaServiceLink = "https://bit.ly/2qTY540"
bmwServiceLink = "https://bit.ly/2oZwQDg"
audiServiceLink = "https://audi.us/2qRXtvC"


gabrielleTwilioInfo = {}
gabrielleTwilioInfo["account_sid"] = "ACbc5842ec489c7a7407796bf39f2121e4" 
gabrielleTwilioInfo["auth_token"] = "f55be7e0c90e9618b4251b806f77467d" 
gabrielleTwilioInfo["twilio_number"] = "+18434597340" 
gabrielleTwilioInfo["phone_number"] = "+18439573064" 

cameronTwilioInfo = {}
cameronTwilioInfo["account_sid"] = "ACcbfca0d2bdd930996875de37745ad9de" 
cameronTwilioInfo["auth_token"] = "70ba1477767cb8b6fcc2ef9c87c2769c"
cameronTwilioInfo["twilio_number"] = "+19164617793"
cameronTwilioInfo["phone_number"] = "+19167984145" 


 
def smsMessager(messageBody):
  account_sid = gabrielleTwilioInfo["account_sid"]
  auth_token = gabrielleTwilioInfo["auth_token"]
  client = Client(account_sid, auth_token) 

  message = client.messages.create( 
    from_=gabrielleTwilioInfo["twilio_number"],
    body="SmartMaintain: {0}'.format(messageBody)",         
    to=gabrielleTwilioInfo["phone_number"]
  ) 
  print(message.sid)
