"""
Django Settings Package Initializer

Loads base.py first (shared config), then either dev.py or prod.py depending on DJANGO_ENV.

Expected values:
    DJANGO_ENV=dev    → development mode (loads from .env)
    DJANGO_ENV=prod   → production mode (loads from OS)

Defaults to dev if not set.
"""

import os
from .base import *

# Read environment mode: default to 'dev'
env_mode = os.environ.get("DJANGO_ENV", "dev")

# Dynamically apply the correct settings
if env_mode == "prod":
    from .prod import *
elif env_mode == "dev":
    from .dev import *
else:
    raise ValueError(f"Unknown DJANGO_ENV value: {env_mode}")
 