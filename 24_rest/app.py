from flask import Flask, render_template, request, session, url_for, redirect
import os
import urllib
import json

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/", methods = ["POST", "GET"])
def input_field_page():
	# Please be responsible with my public key :)
	request = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=NWCEFKTu2YHw1yKF6wsI7BqLLc9bvTzQD3rLUm4s')
	data = json.loads(request.read())
	videoUrl = data['url']
	explanation = data['explanation']
	return render_template('nasa.html', image = videoUrl, description = explanation)

if __name__ == "__main__":
	app.debug = True
	app.run()
