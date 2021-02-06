
## FizzBuzz Fun!

This application is currently accessible at
[fizzbuzzfun.duckdns.org](https://fizzbuzzfun.duckdns.org)

## Implemententation

- Flask
- Python
- Apache2

## Contribute!
Contribute to this repository by submitting a PR!

## Running

- Running on your local machine:
	1. Clone this application to a reasonable location.
	2. Run `cd fizz_buzz_fun`,
	3. `python3 -m venv venv`,
	4. `source venv/bin/activate`,
	5. `pip install -r requirements.txt`,
	6. `export FLASK_APP=FizzBuzz`, then
	7. `flask run`.

- The application will be viewable in your browser at [localhost:5000](localhost:5000). You can run `export FLASK_DEBUG=1` if you want to debug the application.

- You can configure the application to run on an Apache server. We recommend reading the documentation on how to do this [here](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps).
