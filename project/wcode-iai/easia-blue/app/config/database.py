import pyodbc
from app.config.config import settings


def get_db_connection():
  conn_str = (
    f"DRIVER={{{settings.DB_DRIVER}}};"
    f"SERVER={settings.DB_SERVER};"
    f"DATABASE={settings.DB_DATABASE};"
    f"UID={settings.DB_USER};"
    f"PWD={settings.DB_PASSWORD}"
  )
  connection = pyodbc.connect(conn_str)
  return connection
