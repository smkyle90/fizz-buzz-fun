
# FizzBuzz Fun!

This is an application that allows you to see *an* implementation of FizzBuzz, but not so much for the actual algorithmic implementation, but for some interesting and/or useful tools that are required to build a *simple* application.

The purpose is to be an open source Flask and Python project that anyone can contribute to to show the beauty of building software. The first implementation of this is uses Python to solve the FizzBuzz problem, but not only for "Fizz" and associated divisor 3, and "Buzz" and 5, but for any combination of word and divisor, like "Foo" and 2 and "Bar" and 7. Neat!

This application is currently accessible at [fizzbuzzfun.duckdns.org](https://fizzbuzzfun.duckdns.org).

## Implemententation
- Flask
- Python
- Apache2

## Running
- Running on your local machine:
	```
	git clone https://github.com/smkyle/fizz_buzz_fun.git
	cd fizz_buzz_fun
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	export FLASK_APP=FizzBuzz
	flask run
	```

- The application will be viewable in your browser at [localhost:5000](localhost:5000). You can run `export FLASK_DEBUG=1` if you want to debug the application.

- You can configure the application to run on an Apache server. We recommend reading the documentation on how to do this [here](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps).

## Contribute!
Contribute to this repository by submitting a PR!
