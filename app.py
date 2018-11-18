from flask import Flask, render_template, url_for, redirect, request, session, jsonify
import json

import smartcar
import apiHelperFunctions  # imported for the clientInstance variable 

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=["GET", "POST"])
def home():
	authURL = apiHelperFunctions.clientInstance.get_auth_url(force=True)
	return render_template('index.html', title="Home", authURL = authURL)

@app.route('/callback', methods=['GET'])
def callback():
	code = request.args.get('code')
	if code == "access_denied" or code == None:
		return render_template("deniedPermissions.html", title="Denied Permissions")
	access = apiHelperFunctions.clientInstance.exchange_code(code)
	
	return redirect(url_for("dashboard", accessToken=access))

@app.route('/dashboard/<accessToken>', methods=["GET", "POST"])
def dashboard(accessToken):
	accessToken = apiHelperFunctions.FreshAccessToken(accessToken)  # in case its expired
	vehicles = apiHelperFunctions.GetVehicles(accessToken["access_token"])
	vehicleID = vehicles[0]  # always takes the first vehicle
	vehicle = smartcar.Vehicle(vehicleID, accessToken["access_token"])

	odometer = vehicle.odometer()
	location = vehicle.location()
	info = vehicle.info()
	print(location)
	print(odometer)
	print(info)
	print("\n\n\n")

	return render_template("dashboard.html", title="dashboard")

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
