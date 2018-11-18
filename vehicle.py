class Vehicle:
  def __init__(self, idInput, make, model, year, odometer, location, accessToken):
    self.id = idInput
    self.make = make
    self.model = model
    self.year = year
    self.teslaAirFilterLifespan = 25000
    self.brakePadLifespan = 70000
    self.batteryLifespan = 54000
    self.windshieldWiperLifespan = 13500
    self.odometer = odometer
    self.location = location # tuple(latitude, longitude)
    self.accessToken = accessToken

  def VehicleToDict(self):
    dictInstance = {}
    dictInstance['id'] = self.id
    dictInstance['make'] = self.make
    dictInstance['model'] = self.model
    dictInstance['year'] = self.year
    dictInstance['teslaAirFilterLifespan'] = self.teslaAirFilterLifespan
    dictInstance['brakePadLifespan'] = self.brakePadLifespan
    dictInstance['batteryLifespan'] = self.batteryLifespan
    dictInstance['windshieldWiperLifespan'] = self.windshieldWiperLifespan
    dictInstance['odometer'] = self.odometer
    dictInstance['location'] = str(self.location)
    dictInstance['accessToken'] = self.accessToken
    return dictInstance


  def getModel(self):
    return self.model

  def getCurrentLocation(self):
    return self.location[-1]

  def getCurrentOdometerReading(self):
    return self.odometer[-1]

  def getTeslaAirFilterLifespan(self):
    return self.teslaAirFilterLifespan
  
  def getBrakePadLifespan(self):
    return self.brakePadLifespan
  
  def getBatteryLifespan(self):
    return self.batteryLifespan

  def getWindshieldWiperLifespan(self):
    return self.windshieldWiperLifespan

  def updateLocation(self, location):
    self.location.append(location)
  
  def updateOdometerReading(self, odometer):
    self.odometer.append(odometer)
  
  def setTeslaAirFilterLifespan(self, teslaAirFilterLifespan):
    self.teslaAirFilterLifespan = teslaAirFilterLifespan
  
  def setBrakePadLifespan(self, brakePadLifespan):
    self.brakePadLifespan = brakePadLifespan

  def setBatteryLifespan(self, batteryLifespan):
    self.batteryLifespan = batteryLifespan

  def setWindshieldWiperLifespan(self, windshieldWiperLifespan):
    self.windshieldWiperLifespan = windshieldWiperLifespan

  def decreaseWindshieldWiperLifespan(self, lifespan):
    self.windshieldWiperLifespan -= lifespan

  def decreaseTeslaAirFilterLifespan(self, lifespan):
    self.teslaAirFilterLifespan -= lifespan

  def decreaseBatteryLifespan(self, lifespan):
    self.batteryLifespan - lifespan

  def decreasebrakePadLifespan(self, lifespan):
    self.brakePadLifespan - lifespan

# vehicleTest = Vehicle(12455, "Tesla", "S3", 2018, 50000, (38.665266, -121.391185), None)
# print(vehicleTest.VehicleToDict())

# print(eval((vehicleTest.VehicleToDict())['location']))