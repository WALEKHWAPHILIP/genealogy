"""
Base Django Settings

Contains settings shared by all environments (development and production).
This file should NOT include any secrets or environment-specific configuration.
"""

from pathlib import Path

# Base directory of the Django project
BASE_DIR = Path(__file__).resolve().parent.parent

# Hosts allowed to serve the project
ALLOWED_HOSTS = []

# Installed Django and custom apps
INSTALLED_APPS = [
    # Django defaults
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'simple_history',

    # Custom apps (explicit config)
    'users.apps.UsersConfig',
    'people.apps.PeopleConfig',
    'relationships.apps.RelationshipsConfig',
    'events.apps.EventsConfig',
    'narratives.apps.NarrativesConfig',
    'documents.apps.DocumentsConfig',
    'admin_tools.apps.AdminToolsConfig',
]

# Middleware stack (including version history tracking)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'geneology.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Templates directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'geneology.wsgi.application'

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True

# Static and media file configuration
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

# Auto-generated primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
