from .base_settings import BaseConfig


class ProdConfig(BaseConfig):
  DB_SERVER: str = "prod-db-server"
  DB_DATABASE: str = "easia_blue_prod"
  DB_USER: str = "prod_user"
  DB_PASSWORD: str = "prod_password"

  HOST: str = "0.0.0.0"
  PORT: int = 80
  ENV: str = "production"
