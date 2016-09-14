from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)

# Use a secure, unique and absolutely secret key for
# signing the data.
WTF_CSRF_SECRET_KEY = config('WTF_CSRF_SECRET_KEY')
SECRET_KEY = config('SECRET_KEY')
