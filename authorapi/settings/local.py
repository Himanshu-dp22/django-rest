import imp
from .base import *
from .base import env

DEBUG = True

SECRET_KEY = env("DJANGO_SECRET_KEY",default='django-insecure-+2i!wpo$#8mxjk!r%e9x@y7(^=x*4=6y03%2xiw_g-d$ar2o0w')
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]