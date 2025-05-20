from .base_settings import BaseConfig


class DevConfig(BaseConfig):
  DB_SERVER: str = "localhost"
  DB_DATABASE: str = "easia_blue_dev"
  DB_USER: str = "dev_user"
  DB_PASSWORD: str = "dev_password"

  HOST: str = "127.0.0.1"
  PORT: int = 8901
  ENV: str = "development"
