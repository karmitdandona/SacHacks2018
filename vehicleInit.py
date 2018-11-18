"""
* make a function where you're given a vehicle ID and an accessToken and you check a file for if it exists (structure this file as a .py that's a dict, where key is vehicle ID and value is the vehicle class instance)
* if it exists, return the instance of the vehicle
* if it doesn't exist, then you call a different function to initialize a Vehicle instance using the vehicle ID and accessToken

here's some helpful stuff for that second function:

vehicle = smartcar.Vehicle(vehicleID, accessToken["access_token"])
location = vehicle.location()
odometer = vehicle.odometer()
info = vehicle.info()

examples:
{'data': {'latitude': 37.07706832885742, 'longitude': -108.27452087402344}, 'age': datetime.datetime(2018, 11, 18, 3, 16, 12, 579000, tzinfo=tzutc())}
{'data': {'distance': 44376.44140625}, 'unit_system': 'metric', 'age': datetime.datetime(2018, 11, 18, 3, 16, 12, 339000, tzinfo=tzutc())}
{'id': 'bf67d922-1e8a-4eb3-bffe-475feaee8e4e', 'make': 'TESLA', 'model': 'Model S', 'year': 2016}


Also we need an update function (given a vehicle ID and a vehicle instance, update the dictionary's vehicle ID with the new vehicle instance)
"""
import json
from vehicle import Vehicle

"""Creates vehicle dictionary when data.json is empty"""
def vehicleInit(vehicleId, vehicle):
  storedDict = {}
  storedDict[vehicleId] = vehicle

  with open('data.json', 'w') as outfile:
    json.dump(storedDict, outfile)

"""Returns the data from data.json as a dictionary"""
def getVehicleDataAsDict():
  with open('data.json', 'r') as infile:
    storedJson = json.load(infile)
  return storedJson


"""Pushes a new vehicile on the dictionary"""
def updateDictionary(vechicleId, vehicle):
  
  # pull in json and read in dictionary
  storedDict = getVehicleDataAsDict()

  # push to dictionary 
  storedDict[vechicleId] = vehicle

  # write to json file as json
  with open('data.json', 'w') as outfile:
    json.dump(storedDict, outfile)

def toVehicleInstance(id, json):

  vehicle = Vehicle(json[id]["id"], json[id]["make"], json[id]["model"], json[id]["year"], json[id]["odometer"],eval(json[id]["location"]), json[id]["accessToken"])
  vehicle.setTeslaAirFilterLifespan(json[id]["teslaAirFilterLifespan"])
  vehicle.setBrakePadLifespan(json[id]["brakePadLifespan"])
  vehicle.setBatteryLifespan(json[id]["batteryLifespan"])
  vehicle.setWindshieldWiperLifespan(json[id]["windshieldWiperLifespan"])
  return vehicle
