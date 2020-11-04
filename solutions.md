# Project Purple Cow

This project was built by Caleb M. Godwin for Fearless. It is a simple server that provides one or more buttons that, when clicked, hit the [CountAPI](https://countapi.xyz/) API and display the results.

## Prerequisites

To successfully run this project, you must have the following on your system:
* A GNU/Linux distribution with root access. macOS has not been tested, but may work.
* Docker
* Python
* Bash

## Running Automatically

Before running, please ensure that you add your API keys to `ProjectPurpleCow/config.json`. See [Configuration](#configuration) and [Test API Keys](#test-api-keys).

This project uses Docker and provides a simple shell script to build and run the project automatically. Before running, make sure you have [all prerequisites](#prerequisites) installed on your system. Then simply clone this repository, `cd` into the project's directory root, and execute:

	# ./start.sh
If you receive permission errors, run `# chmod +x start.sh` and try again. When all goes well, you will receive output stating:

	Project Purple Cow is running on port [your port]. To stop, use "sudo docker stop [id]" where [id] is (at least part of) the container ID shown above.

If the Docker container exits prematurely, you may then run:

	# sudo docker logs [id]

Where `[id]` is the container ID shown or retrieved using `# docker ps`.

## Running Manually

Instead of using `start.sh`, you may opt to build and run the Docker container manually. To do this, execute the following commands at your terminal:

	# sudo docker build -t projectpurplecow:latest .
	# sudo docker run -d -p [port]:[port] projectpurplecow

Where `[port]` is the port defined in `ProjectPurpleCow/config.json`. The default is port 3000.

## Configuration

This project's configuration file is located at `ProjectPurpleCow/config.json` relative to the project root. This JSON file contains several editable parameters.
* "port" -- the port the project should expose to the world, default is 3000
* "host" -- the host to bind to, default is "0.0.0.0"

The "buttons" object contains API keys for CountAPI mapped to button names. Each button you wish to implement must have a unique name and an associated API key. For example:

	"buttons": {
		"button1": "example_key_1",
		"button2": "example_key_2",
		. . .
	}
Please note that from a security perspective, it is unwise to commit API keys to code repositories unless absolutely necessary.

## Test API Keys

For the test case, it is acceptable to add the following keys to `ProjectPurpleCow/config.json`:
* For button 1, use `1ccb732e-b55a-4404-ad3f-0f99c02fe44e`
* For button 2, use `dkgrv7rr-qkxu-3m25-pa9j-tdkqar5u7jga`
* For button 3, use `4ctuy8tt-7pob-bvas-72do-uzjz937c7waz`

Make sure that each key is in quotes in the configuration file, as they are strings!

## Adding More Buttons

The code handling the button is fully reusable. You may add as many as you wish, as long as each has a valid API key as shown above. To add a button in an HTML file with Bootstrap styling, the following will work:

	<button type="button" class="btn btn-primary" id="YOUR_ID_HERE">This is a button</button>

Make sure to replace `YOUR_ID_HERE` with the button's ID defined in configuration. In the head of your document, add the following (omitting any lines already present):

	<script src="/path/to/button.js"></script> <!-- import register_button() -->
	<script>
		$(document).ready(function() {
			register_button("YOUR_ID_HERE", function(response) {
				//Do something here with the results!
			});
		});
	</script>
If you are using the button script within the framework of this project specifically, replace `/path/to/button.js` with `{{ url_for('static', filename='button.js') }}`. Flask will fill in this path automatically.

The content of `response` will be text containing either the result or some error if thrown.

## Future Updates

1. It would be prudent to generalize the API endpoint. Instead of hard-coding `https://api.countapi.xyz/hit/` this could be an option in the configuration file with a custom parser to determine, for example, where to put the key.
2. Improve configuration management to allow for live updates to the config file without having to stop and start the server.
3. Improve error handling. Some blocks are left as `except Exception as e` or even just `except`. While it is acceptable to state that this is not *wrong* per-se, it is less verbose and potentially leaves some specific error cases to be handled in a generic way.
4. Add configurable logging to disk based on event level (e.g. info, warning, error, etc.)
5. To improve readability as well as make codebase scaling more manageable, move the `/hit/` route in `main.py` to another file.
6. Determine which Bootstrap CSS and JavaScript files (located in `static/css` and `static/js`) are needed and throw away the rest to reduce project footprint.

## Assumptions and Details

1. This project was written in the Flask framework due the small size. If the project is to scale up to large or very-large size, it may be wise to move to a framework that is more apt to support such projects, such as Django.
2. This was written with security in mind. As such, the button click event sends a request to the `/hit/` endpoint on the server, which then picks up the relevant API key from configuration and then sends a request to CountAPI. This prevents the API key from being exposed to the public. However, this could be problematic at scale as each request requires two HTTP requests. Depending upon the level of security needed, it could be wise to move the CountAPI call to pure JavaScript.
3. Flask uses the Jinja2 template rendering engine. In this project, `base.html` contains generic markup and provides blocks to fill in, and each file extends from that. To create a document with a completely new style it will be necessary to either create a different template or change the existing one.
4. The program is designed to run on Linux only and may work on macOS. Windows is not currently supported, however this could likely be achieved with relative ease.
