from .base import *

from socket import gethostbyname
from socket import gethostname

DEBUG = False

SECRET_KEY = env["SECRET_KEY"]

ALLOWED_HOSTS = env.get("ALLOWED_HOST").split(",")
ALLOWED_HOSTS.append(gethostbyname(gethostname()))

try:
    from .local import *
except ImportError:
    pass
