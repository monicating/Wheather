from flask import Flask, render_template, request

import  pywapi
import string

app = Flask(__name__)
app.config["DEBUG"] = True  # Only include this while you are testing your app

@app.route("/")
def hello():
	return render_template("index.html")

@app.route("/monica")
def name():
	return "Monica"

@app.route("/search/<search_query>")
def search(search_query):
	return search_query

@app.route("/add/<x>/<y>")
def add(x,y):
	return str(int(x) + int(y))

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry, this page was not found.", 404

@app.route("/weather", methods=["GET", "POST"])
def weather():
	if request.method == "POST":
		zip = request.form["user_search"]
		weather_com_result = pywapi.get_weather_from_weather_com(zip)
		#return "Weather.com says: It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in " + zip
		return render_template("results.html", api_data=weather_com_result)
	else: # GET
		return render_template("search.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")

