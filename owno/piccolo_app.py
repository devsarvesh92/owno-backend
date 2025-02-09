"""
Import all of the Tables subclasses in your app here, and register them with
the APP_CONFIG.
"""

import os

from piccolo.conf.apps import AppConfig
from src.models import User, RealEstateProperty, UserFavoriteProperty

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


APP_CONFIG = AppConfig(
    app_name="owno",
    migrations_folder_path=os.path.join(CURRENT_DIRECTORY, "piccolo_migrations"),
    table_classes=[User, RealEstateProperty, UserFavoriteProperty],
    migration_dependencies=[],
    commands=[],
)
