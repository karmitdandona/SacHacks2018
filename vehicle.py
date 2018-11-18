import sendSms

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
    self.textSent = {"airFilter": False, "brakePad": False, "battery": False, "windshieldWiper": False}

  def SendText(self, keyToSendFor):
    messageEnd = " miles remaining! Schedule Appointment: "
    if self.make == "TESLA":
      messageEnd += sendSms.teslaServiceLink
    elif self.make == "BMW":
      messageEnd += sendSms.bmwServiceLink
    elif self.make == "AUDI":
      messageEnd += sendSms.audiServiceLink

    if keyToSendFor == "airFilter":
      sendSms.smsMessager("Air filter maintenance required, " + str(self.teslaAirFilterLifespan) + messageEnd) 
      self.textSent["airFilter"] = True
    elif keyToSendFor == "brakePad":
      sendSms.smsMessager("Brake pad maintenance required, " + str(self.brakePadLifespan) + messageEnd)
      self.textSent["brakePad"] = True
    elif keyToSendFor == "battery":
      sendSms.smsMessager("Battery maintenance required, " + str(self.batteryLifespan) + messageEnd)
      self.textSent["battery"] = True
    elif keyToSendFor == "windshieldWiper":
      sendSms.smsMessager("Windshield wiper maintenance required, " + str(self.windshieldWiperLifespan) + messageEnd)
      self.textSent["windshieldWiper"] = True
    return


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
    dictInstance['textSent'] = self.textSent
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
