from app import create_app
import os
import config

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
application=create_app(os.path.join(BASE_DIR, 'config.py'))
application.run(port=config.PORT)

