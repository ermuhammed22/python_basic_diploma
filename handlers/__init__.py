from . import custom_handlers
from . import default_handlers
from api import api


def get_api_instance():
    return api.api
