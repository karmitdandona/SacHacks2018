"""
* make a function where you're given a vehicle ID and an accessToken and you check a file for if it exists (structure this file how you want, make it a json or a .py file with an array of Vehicles)  --> probably an array of vehicle instances in a .py file is best
* if it exists, return the instance of the vehicle
* if it doesn't exist, then you call a different function to initialize a Vehicle instance using the vehicle ID and accessToken

here's some helpful stuff for that second function:

vehicle = smartcar.Vehicle(vehicleID, accessToken["access_token"])
odometer = vehicle.odometer()
location = vehicle.location()
info = vehicle.info()
"""