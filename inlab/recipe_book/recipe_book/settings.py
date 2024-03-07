# recipe_book/settings.py
# Add the following lines at the end of the file
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'
# recipe_book/settings.py
# Add the following line to the end of the file
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
