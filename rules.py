from vehicle import Vehicle

vehicleInfo = Vehicle(12455, "Tesla", "S3", 2018, 50000, (38.665266, -121.391185))

def manipulateTeslaAirFilter(airQuality):
  filterStatus = vehicleInfo.getTeslaAirFilterLifespan()
  vehicleInfo.setTeslaAirFilterLifespan(filterStatus - airQuality * 0.03)

def manipulateBrakePad():
  brakeStatus = vehicleInfo.getBrakePadLifespan()
  vehicleInfo.setBrakePadLifespan(brakeStatus - 42)

def manipulateBattery():
  batteryStatus = vehicleInfo.getBatteryLifespan()
  vehicleInfo.setBatteryLifespan(batteryStatus - 19)

def manipulateWindshieldWiper():
  wiperStatus = vehicleInfo.getWindshieldWiperLifespan()
  vehicleInfo.setWindshieldWiperLifespan(wiperStatus - 18)

def executeRules(airQuality, tempurature, climate):
  if tempurature <= 32:
    manipulateBrakePad()
  if climate == "Drizzle" or climate == "Rain" or climate == "Snow":
    manipulateWindshieldWiper()

  if vehicleInfo.getModel() == "Tesla":
    if airQuality > 100:
      manipulateTeslaAirFilter(airQuality)
  else:
    if tempurature <= 32:
      manipulateBattery()
