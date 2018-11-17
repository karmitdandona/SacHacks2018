from flask import Flask, render_template, url_for, redirect, request, session, jsonify
import json


app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=["GET", "POST"])
def home():
	return render_template('index.html', title="Home")

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
