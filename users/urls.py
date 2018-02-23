from lib.urls.patterns import path
from .views import index


urlpatterns = [
    path('', 'index', view_func=index),
]