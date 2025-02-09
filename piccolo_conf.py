from piccolo.engine.postgres import PostgresEngine


from piccolo.conf.apps import AppRegistry

from src.settings import settings


DB = PostgresEngine(
    config={
        "database": settings.DB_NAME,
        "user": settings.DB_USER,
        "password": settings.DB_PASSWORD,
        "host": settings.DB_HOST,
        "port": settings.DB_PORT,
    }
)


APP_REGISTRY = AppRegistry(apps=["owno.piccolo_app"])
