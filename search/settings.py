# SETTINGS FILE
import os


# ROOT DIRECTORY
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# TEMPLATES ROOT DIRECTORY
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates/')

# DATABASE
DATABASE_URI = 'sqlite:////tmp/test.db'

APP_MODULES = [
    'users',
] 