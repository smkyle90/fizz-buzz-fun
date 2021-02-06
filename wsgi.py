# pylint: skip-file   (newer)
# flake8: noqa

"""App entry point."""

import sys

# Add this to ensure we are in the correct directory to avoid an import error
sys.path.insert(0, "/var/www/FizzBuzz")

from FizzBuzz import create_app  # pylint: disable=no-name-in-module flake8: noqa

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
