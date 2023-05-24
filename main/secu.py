
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
# security.W016
CSRF_COOKIE_SECURE = True

# security.W012
SESSION_COOKIE_SECURE = True

# security.W008
SECURE_SSL_REDIRECT = True

# security.W004
SECURE_HSTS_SECONDS = 31536000 # One year in seconds

# Another security settings
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# security.W022
# I think it won't be needed. Because there are many ways.