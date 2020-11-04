import json
from main import app

# Attempt to retrieve value for key in config file
# This is for critical configuration info, so program will exit if it fails
# convert_func must be a function that converts one value to another, e.g. "str" or "int"
def try_get_key(config, key, convert_func):
    try:
        return convert_func(config[key])
    except KeyError: # Key does not exist
        print("Could not find \"{}\" key in your configuration! Add this key-value pair and try again.".format(key))
        quit()
    except ValueError: # Value cannot be converted to the requested type (specified by convert_func)
        print("Value for key \"{}\" in your configuration is not valid! Fix this and try again.".format(key))
        quit()
    except Exception as e: # Some other bad thing happened
        print("An error occured while trying to read key \"{}\" in your configuration! Error was: \"{}\".".format(key, e))
        quit()

# Load configuration file
try:
    config = json.load(open("config.json", 'r'))
except FileNotFoundError:   # "config.json" does not exist
    print("Failed to open \"config.json\"! Check this file and try again.")
    quit()
except json.decode.JSONDecodeError: # File is not formatted correctly
    print("Failed to parse \"config.json\"! Check JSON syntax and try again.")
    quit()

# Retrieve needed values from config
port = try_get_key(config, "port", int)
host = try_get_key(config, "host", str)

# Run the application
app.run(port=port, host=host)
