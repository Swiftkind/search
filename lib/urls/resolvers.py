from search.settings import APP_MODULES
from search.urls import urlpatterns

from lib.urls.patterns import url



def urlresolver(app):
    for app_label, _file in urlpatterns:
        app_label, bp = url(app_label, _file)
        app.register_blueprint(bp)

    return app