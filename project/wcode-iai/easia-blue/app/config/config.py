import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
  DB_SERVER: str = os.getenv("DB_SERVER")
  DB_DATABASE: str = os.getenv("DB_DATABASE")
  DB_USER: str = os.getenv("DB_USER")
  DB_PASSWORD: str = os.getenv("DB_PASSWORD")
  DB_DRIVER: str = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")

  HOST: str = os.getenv("HOST", "0.0.0.0")
  PORT: int = int(os.getenv("PORT", 8901))


settings = Settings()
