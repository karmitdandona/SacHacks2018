import smartcar
import schedule
import time
import json

import vehicleInit
import apiHelperFunctions
import vehicle
import rules
import weather
import airquality

def UpdateAllVehicles():
  vehicleDict = vehicleInit.getVehicleDataAsDict()
  for key,val in vehicleDict.items():
    # --- GET NEW INFORMATION (NEW QUERY) --- #
    accessToken = val["accessToken"]
    # accessToken = apiHelperFunctions.RefreshAccessToken(accessToken)  # it'll probably be expired
    vehicle = smartcar.Vehicle(key, accessToken)
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
    aiqDict = airquality.GetAiq(currentLongitude, currentLatitude)
    updatedInstance = rules.executeRules(curInstance, aiqDict['aiq'], weatherDict["temp"], weatherDict["climate"])

    # put the updated vehicle back into dict
    vehicleDict[key] = updatedInstance.VehicleToDict()

  print("update successful")
  with open('data.json', 'w') as outfile:
    json.dump(vehicleDict, outfile)

def main():
  # schedule.every().hour.do(UpdateAllVehicles)
  schedule.every().minute.do(UpdateAllVehicles)  # for testing
  while True:
    schedule.run_pending()
    time.sleep(1)
  

if __name__ == '__main__':
	main()
