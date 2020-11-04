#!/bin/bash

# Build the project
echo Building Project Purple Cow...
sudo docker build -t projectpurplecow:latest .

# Retrieve desired port from config file
PORT=$(python3 -c "import json; print(json.load(open('ProjectPurpleCow/config.json', 'r'))['port'])")
[ -n "$PORT" ] && [ "$PORT" -eq "$PORT" ] 2>/dev/null # Check if $PORT is a valid number
if [ $? -ne 0 ]; then
    echo
    echo
    echo Failed to retrieve port from project configuration file. Please check it and try again!
    exit
fi

# Run the project
sudo docker run -d -p $PORT:$PORT projectpurplecow
echo 
echo 
echo Project Purple Cow is running on port $PORT. To stop, use \"sudo docker stop [id]\" where [id] is \(at least part of\) the container ID shown above.
