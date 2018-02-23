import os

from flask import Blueprint
from search.settings import APP_MODULES, TEMPLATES_DIR


class Pattern(object):
    """ need to make the APP_LABEL dynamic
    """
    def __init__(self, app, *args, **kwargs):
        self.app = app
        return super(Pattern, self).__init__()

    def load(self):
        return Blueprint(self.app, __name__, template_folder=TEMPLATES_DIR)


def path(pattern, name, view_func):
    return pattern, name, view_func


def url(pattern, _file):
    module = __import__(_file)
    app_label, f = _file.split(".")

    bp = Pattern(app=app_label).load()

    for path, name, view_func in module.urls.urlpatterns:
        abspath = f"{pattern}{path}"
        bp.add_url_rule(abspath, name, view_func=view_func)

    return app_label, bp


    

