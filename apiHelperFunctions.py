import smartcar
import datetime

clientInstance = smartcar.AuthClient(
  client_id="84eb461b-0576-4cb3-8f5f-5c66d03b8752",
  client_secret="9d066199-06af-48bc-9bcf-2d8111511c51",
  redirect_uri="http://localhost:5000/callback",
  scope=["read_vehicle_info", "read_location", "read_odometer"],
  test_mode=True
)

def FreshAccessToken(oldToken):
  """returns a fresh token if oldToken is expired"""
  tokenDict = eval(oldToken)
  if smartcar.is_expired(tokenDict['expiration']):
    newToken = clientInstance.exchange_refresh_token(tokenDict['refresh_token'])
    return newToken
  else:
    return tokenDict

def GetVehicles(accessToken):
  print(accessToken)
  print(type(accessToken))
  print("\n\n\n")
  vehicles = smartcar.get_vehicle_ids(accessToken)
  return vehicles["vehicles"]
