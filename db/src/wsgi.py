import sys
import os

# add your project directory to the sys.path
project_dir = "/home/wrvbracmarketing/mysite/nexunia/db/src"
sys.path.insert(0, project_dir)

# activate your virtual environment
activate_this = "/home/wrvbracmarketing/.virtualenvs/venv/bin/activate_this.py"
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# import the Flask app
from main import app as application

