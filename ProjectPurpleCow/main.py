import requests

from flask import Flask, render_template

from Utilities import get_config

app = Flask(__name__)

@app.route("/")
def index():
    try:
        config = get_config()
        return render_template("index.html")
    except Exception as e:
        return render_template("error.html", error="There was a problem with the application's configuration file.", error_content=str(e))

@app.route("/hit/<string:button_id>")
def hit(button_id):
    try:
        api_key = get_config()["buttons"][button_id]
    except:
        return "API key for {} was not found!".format(button_id)
    
    try:
        response = requests.get("https://api.countapi.xyz/hit/{}".format(api_key))
    except Exception as e:
        return "Error occured while trying to hit API: {}".format(e)

    if response.status_code != 200 and response.status_code != 400:
        return "API returned status code {}!".format(response.status_code)
    
    try:
        response_json = response.json()
    except:
        return "API returned non-JSON response!"

    if "error" in response_json:
        return "API returned error: {}".format(response_json["error"])
    elif "value" in response_json:
        return "Number of hits is {}.".format(response_json["value"])
    else:
        return "Unrecognized response from API!"
    