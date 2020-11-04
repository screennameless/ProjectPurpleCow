import requests
from flask import Flask, render_template

from Utilities import get_config

app = Flask(__name__)

# Route for root
@app.route("/")
def index():
    try:
        config = get_config()
        return render_template("index.html")
    except Exception as e:
        return render_template("error.html", error="There was a problem with the application's configuration file.", error_content=str(e))

# Route for /hit/... takes button_id parameter that must match API keys in config.json
@app.route("/hit/<string:button_id>")
def hit(button_id):
    # Attempt to retrieve API key from config
    try:
        api_key = get_config()["buttons"][button_id]
    except:
        return "API key for {} was not found!".format(button_id)
    
    # Send HTTPS request to API
    try:
        response = requests.get("https://api.countapi.xyz/hit/{}".format(api_key))
    except Exception as e:
        return "Error occured while trying to hit API: {}".format(e)

    # Response code must be 200 or 400 to keep processing
    if response.status_code != 200 and response.status_code != 400:
        return "API returned status code {}!".format(response.status_code)
    
    # Convert response to JSON
    try:
        response_json = response.json()
    except:
        return "API returned non-JSON response!"

    if "error" in response_json: # API returned error
        return "API returned error: {}".format(response_json["error"])
    elif "value" in response_json: # Everything is fine!
        return "Number of hits is {}.".format(response_json["value"])
    else: # Catch-all
        return "Unrecognized response from API!"
    