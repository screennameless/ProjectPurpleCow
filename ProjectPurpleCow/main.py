from flask import Flask, render_template

from Utilities import get_config

app = Flask(__name__)

@app.route("/")
def index():
    try:
        config = get_config()
        return render_template("index.html", api_key=config["api_key"])
    except Exception as e:
        return render_template("error.html", error="There was a problem with the application's configuration file.", error_content=str(e))
        
    