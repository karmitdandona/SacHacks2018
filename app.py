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

@app.route('/callback', methods=['GET'])
def callback():
	code = request.args.get('code')
	if code == "access_denied" or code == None:
		return render_template("deniedPermissions.html", title="Denied Permissions")
	access = apiHelperFunctions.clientInstance.exchange_code(code)
	
	return redirect(url_for("dashboard", accessToken=access["access_token"]))

@app.route('/dashboard/<accessToken>', methods=["GET", "POST"])
def dashboard(accessToken):
	# accessToken = apiHelperFunctions.RefreshAccessToken(accessToken)
	vehicles = apiHelperFunctions.GetVehicles(accessToken)
	vehicleID = vehicles[0]  # always takes the first vehicle
	
	tempVehicle = vehicleInit.FindVehicleInstance(vehicleID, accessToken)

	return render_template("dashboard.html", title="dashboard")

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
