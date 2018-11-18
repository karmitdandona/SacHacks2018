class Vehicle:
  def __init__(self, id, make, model, year, odometer, location):
    self.id = id
    self.make = make
    self.model = model
    self.year = year
    self.testlaAirFilterLifespan = 27000
    self.brakePadLifespan = 70000
    self.batteryLifespan = 54000
    self.windshieldWiperLifespan = 13500
    self.odometer = [odometer]
    self.location = [location] # tuple(longitude, latitude)

  def getModel(self):
    return self.model

  def getCurrentLocation(self):
    return self.location[-1]

  def getCurrentOdometerReading(self):
    return self.odometer[-1]

  def getTeslaAirFilterLifespan(self):
    return self.testlaAirFilterLifespan
  
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
    self.testlaAirFilterLifespan = teslaAirFilterLifespan
  
  def setBrakePadLifespan(self, brakePadLifespan):
    self.brakePadLifespan = brakePadLifespan

  def setBatteryLifespan(self, batteryLifespan):
    self.batteryLifespan = batteryLifespan

  def setWindshieldWiperLifespan(self, windshieldWiperLifespan):
    self.windshieldWiperLifespan = windshieldWiperLifespan

    