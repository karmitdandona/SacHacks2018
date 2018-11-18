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

gabrielle2TwilioInfo = {}
gabrielle2TwilioInfo["account_sid"] = "ACbdbeafe9fc1abbbabd58be053c45d2a0" 
gabrielle2TwilioInfo["auth_token"] = "36153bb7da6278ad54d6b3e435f7960b"
gabrielle2TwilioInfo["twilio_number"] = "+18434926522"
gabrielle2TwilioInfo["phone_number"] = "+18439573064" 

gabrielle3TwilioInfo = {}
gabrielle3TwilioInfo["account_sid"] = "ACcdb307f02363e0e8f8acfbb993cdf2f5" 
gabrielle3TwilioInfo["auth_token"] = "6d3dc5a29665fe24c41770976f5348f0"
gabrielle3TwilioInfo["twilio_number"] = "+18432865878"
gabrielle3TwilioInfo["phone_number"] = "+18439573064" 

gabrielle4TwilioInfo = {}
gabrielle4TwilioInfo["account_sid"] = "ACe07c26ea526cb3ef0ba20adf9ec07acc" 
gabrielle4TwilioInfo["auth_token"] = "73c8f3920acbd012a9b2ccece9be4dfb"
gabrielle4TwilioInfo["twilio_number"] = "+18432865874"
gabrielle4TwilioInfo["phone_number"] = "+18439573064" 

gabrielle5TwilioInfo = {}
gabrielle5TwilioInfo["account_sid"] = "ACcad0befe96f4ed29fc65a5a0cfdc29b7" 
gabrielle5TwilioInfo["twilio_number"] = "02e97f20a9b13303fe73235009c15f90"
gabrielle5TwilioInfo["twilio_number"] = "+14785594523"
gabrielle5TwilioInfo["phone_number"] = "+18439573064" 
 
def smsMessager(messageBody):
  account_sid = gabrielleTwilioInfo["account_sid"]
  auth_token = gabrielleTwilioInfo["auth_token"]
  client = Client(account_sid, auth_token) 

  message = client.messages.create( 
    from_=gabrielleTwilioInfo["twilio_number"],
    body="SmartMaintain: {0}".format(messageBody),         
    to=gabrielleTwilioInfo["phone_number"]
  ) 
  print(message.sid)
