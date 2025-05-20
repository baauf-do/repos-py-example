from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
  # Cấu hình chung cho mọi môi trường
  DB_DRIVER: str = "ODBC Driver 17 for SQL Server"

  HOST: str = "127.0.0.1"
  PORT: int = 8000

  ENV: str = "development"

  class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"
