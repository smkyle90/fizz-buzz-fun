"""App entry point."""

import sys

print (sys.path,flush=True)

sys.path.insert(0, "/var/www/FizzBuzz")

print (sys.path, flush=True)

from FizzBuzz import create_app  # pylint: disable=no-name-in-module

#print (FizzBuzz.__file__)
application = create_app()

# if __name__ == "__main__":
#     app.run()

"""
ensure tto use venv not pipenv when installing the virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Run this to intialise Db
from oad import db, create_app
db.create_all(app=create_app())
"""
