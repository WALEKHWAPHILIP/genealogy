"""Development Settings

Used when DJANGO_ENV is 'dev' or unset.
Loads environment variables from a local .env file.
"""

import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables into the environment

SECRET_KEY = os.getenv("SECRET_KEY")  # Django secret key
DEBUG = os.getenv("DEBUG", "True").lower() == "true"  # Enable debug mode (default: True)

# PostgreSQL database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}
