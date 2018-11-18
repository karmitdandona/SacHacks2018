import smartcar
import schedule
import time
import json

import vehicleInit
import apiHelperFunctions
import vehicle
import rules
import weather

def UpdateAllVehicles():
  vehicleDict = vehicleInit.getVehicleDataAsDict()
  for key,val in vehicleDict.items():
    # --- GET NEW INFORMATION (NEW QUERY) --- #
    accessToken = val["accessToken"]
    accessToken = apiHelperFunctions.FreshAccessToken(accessToken)  # it'll probably be expired
    vehicle = smartcar.Vehicle(key, accessToken["access_token"])
    currentLocation = vehicle.location()
    currentLatitude = currentLocation["data"]["latitude"]
    currentLongitude = currentLocation["data"]["longitude"]
    currentOdometer = vehicle.odometer()["data"]["distance"]  # assume metric unit system (kilometers)

    # --- UPDATE LOCATION AND ODOMETER ARRAYS OF VEHICLE --- #
    curInstance = vehicleInit.toVehicleInstance(key, val)
    curInstance.updateLocation((currentLatitude, currentLongitude))
    curInstance.updateOdometerReading(currentOdometer)

    # --- MODIFY REMAINING LIFESPANS BASED ON RULES --- #
    weatherDict = weather.GetWeather(currentLongitude, currentLatitude)
    updatedInstance = rules.executeRules(curInstance, 32, weatherDict["temp"], weatherDict["climate"])
    # FIXME add the airQuality parameter to above executeRules call (from airQuality.py)

    # put the updated vehicle back into dict
    vehicleDict[key] = updatedInstance.VehicleToDict()

  
  with open('data.json', 'w') as outfile:
    json.dump(vehicleDict, outfile)

def main():
  schedule.every().hour.do(UpdateAllVehicles)
  # schedule.every().minute.do(UpdateAllVehicles)  # testing
  while True:
    schedule.run_pending()
    time.sleep(1)
  

if __name__ == '__main__':
	main()
