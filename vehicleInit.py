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