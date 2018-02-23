from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from search.settings import DATABASE_URI

db = None

def dbconnect(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    return app