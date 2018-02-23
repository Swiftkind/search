from flask import Flask
from lib.manager import manager, app

from lib.urls.resolvers import urlresolver
from lib.db.connect import dbconnect


if __name__ == "__main__":
    dbconnect(app)
    urlresolver(app)

    manager.run()