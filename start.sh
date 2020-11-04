#!/bin/bash
echo Building Project Purple Cow...
sudo docker build -t projectpurplecow:latest .
echo Running Project Purple Cow...
PORT=$(python3 -c "import json; print(json.load(open('ProjectPurpleCow/config.json', 'r'))['port'])")
sudo docker run -d -p $PORT:$PORT projectpurplecow
echo 
echo 
echo ProjectPurpleCow is running. To stop, use \"sudo docker stop [id]\" where [id] is \(at least part of\) the container ID shown above.
