from flask import Flask, render_template, url_for, redirect, request, session, jsonify
import json

import smartcar
import apiHelperFunctions  # imported for the clientInstance variable
import vehicleInit

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=["GET", "POST"])
def home():
	authURL = apiHelperFunctions.clientInstance.get_auth_url(force=True)
	return render_template('index.html', title="Home", authURL = authURL)

@app.route('/callback', methods=['GET', 'POST'])
def callback():
	code = request.args.get('code')
	if code == "access_denied" or code == None:
		return render_template("deniedPermissions.html", title="Denied Permissions")

	access = apiHelperFunctions.clientInstance.exchange_code(code)

	vehicles = apiHelperFunctions.GetVehicles(access["access_token"])
	vehicleID = vehicles[0]  # always takes the first vehicle
	tempVehicle = vehicleInit.FindVehicleInstance(vehicleID, access["access_token"])  # basically puts the vehicle for selected car manafacturer into the data.json file
	
	# return redirect(url_for("dashboard", vehicleID=vehicleID))
	return redirect(url_for("listVehicles"))

@app.route('/listVehicles', methods=["GET", "POST"])
def listVehicles():
	vehiclesDict = vehicleInit.getVehicleDataAsDict()
	vehicleIDs = []
	for key, val in vehiclesDict.items():
		vehicleIDs.append(key)
	return render_template('listVehicles.html', title="List of Vehicles", vehicleIDs=vehicleIDs)

@app.route('/dashboard/<vehicleID>', methods=["GET", "POST"])
def dashboard(vehicleID):
# 	# accessToken = apiHelperFunctions.RefreshAccessToken(accessToken)
	tempVehicle = vehicleInit.getVehicleDataAsDict()[vehicleID]
	return render_template("dashboard.html", title="Dashboard", data=tempVehicle)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
