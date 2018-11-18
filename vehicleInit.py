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
import smartcar

from vehicle import Vehicle

def FindVehicleInstance(vehicleID, accessToken):
  """check if it exists in json file. if so, return that. if not, make new instance in that json"""
  vehiclesDict = getVehicleDataAsDict()
  if vehicleID in vehiclesDict:
    return toVehicleInstance(vehicleID, vehiclesDict[vehicleID])  # return the vehicle instance (already in data.json)
  else:
    # doesn't exist in data.json, we'll add it into there
    vehicle = smartcar.Vehicle(vehicleID, accessToken)
    vehicleInfo = vehicle.info()
    vehicleOdometer = vehicle.odometer()['data']['distance']
    vehicleLatitude = vehicle.location()['data']['latitude']
    vehicleLongitude = vehicle.location()['data']['longitude']
    newVehicleInstance = Vehicle(vehicleID, vehicleInfo['make'], vehicleInfo['model'], vehicleInfo['year'], [vehicleOdometer], [(vehicleLatitude, vehicleLongitude)], accessToken)

    updateDictionary(vehicleID, newVehicleInstance.VehicleToDict())

    return newVehicleInstance

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


"""Pushes a new vehicle (dict) on the dictionary"""
def updateDictionary(vechicleId, vehicle):
  
  # pull in json and read in dictionary
  storedDict = getVehicleDataAsDict()

  # push to dictionary 
  storedDict[vechicleId] = vehicle

  # write to json file as json
  with open('data.json', 'w') as outfile:
    json.dump(storedDict, outfile)

def toVehicleInstance(id, vehicleDict):
  vehicle = Vehicle(vehicleDict["id"], vehicleDict["make"], vehicleDict["model"], vehicleDict["year"], vehicleDict["odometer"],eval(vehicleDict["location"]), vehicleDict["accessToken"])
  vehicle.setTeslaAirFilterLifespan(vehicleDict["teslaAirFilterLifespan"])
  vehicle.setBrakePadLifespan(vehicleDict["brakePadLifespan"])
  vehicle.setBatteryLifespan(vehicleDict["batteryLifespan"])
  vehicle.setWindshieldWiperLifespan(vehicleDict["windshieldWiperLifespan"])
  return vehicle
