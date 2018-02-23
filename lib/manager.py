from flask import Flask
from flask_script import Manager, Server, Shell, Command, Option
from flask_migrate import MigrateCommand

from lib.db.connect import db



app = Flask(__name__)
manager = Manager(app)

# Run the flask server
server = Server(host='0.0.0.0', port=5000, use_debugger=True)
manager.add_command('run', server)

# Run the flask shell
shell = Shell()
manager.add_command('shell', shell)

# Migrate command
manager.add_command('db', MigrateCommand)
