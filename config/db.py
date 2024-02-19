import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
        "default" : {
            "ENGINE":"django.db.backends.sqlite3",
            "NAME":os.path.join(BASE_DIR, "db/sqlite/db.sqlite3"),
        }
}


POSTGRESQL = {
        "default" : {
            "ENGINE" : "django.db.backends.postgresql_psycopg2", # psycopg2 es el driver de PostgresSQL
            "NAME" :"db",
            "USER":"postgres",
            "PASSWORD":"12345678",
            "HOST":"localhost",
            "PORT":"5432"
        }
}
