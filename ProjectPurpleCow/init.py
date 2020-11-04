import json
from main import app

port = 8080 # default port
host = "0.0.0.0" # default host

# Load configuration file
try:
    config = json.load(open("config.json", 'r'))
except FileNotFoundError:   # "config.json" does not exist
    pass
except json.decode.JSONDecodeError: # File is not formatted correctly
    pass

# Retrieve port config value, if it exists
try:
    port = int(config["port"])
except KeyError: # Key "port" does not exist
    pass
except ValueError: # Value for "port" is not an integer
    pass

# Retrieve host config value, if it exists
try:
    host = str(config["host"])
except KeyError: # Key "host" does not exist
    pass
except ValueError: # Value for "host" cannot be converted to a string
    pass

# Run the application on the port specified in config, or 8080 if not specified
app.run(port=port, host=host)