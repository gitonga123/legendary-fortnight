"""
House configuration that makes use of django-environ module
"""
import environ

env = environ.Env()

TIME_ZONE = env.str("TIME_ZONE", default="Africa/Nairobi")

SECRET_KEY=env.str("SECRET_KEY", default="django-secure-key")

# The url allowed to serve the application
ALLOWED_HOSTS = [
    h.strip()
    for h in env.str("ALLOWED_HOSTS", default="").split(",")
    if h and h.strip()
]
CSRF_TRUSTED_ORIGINS = [
    h.strip()
    for h in env.str("CSRF_TRUSTED_ORIGINS", default="").split(",")
    if h and h.strip()
]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=True)

# Ensure that the csrf cookie is only sent under an HTTPS connection.
CSRF_COOKIE_SECURE = env.bool("SSL_ENABLED", default=False)

# Ensure that the session cookie is only sent under an HTTPS connection.
SESSION_COOKIE_SECURE = env.bool("SSL_ENABLED", default=False)

# Specify the duration of a given session
SESSION_EXPIRE_SECONDS = env.int("SESSION_EXPIRE_SECONDS", default=3600)