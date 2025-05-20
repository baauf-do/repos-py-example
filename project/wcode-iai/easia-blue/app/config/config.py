import os

from .dev_settings import DevConfig
from .prod_settings import ProdConfig


def get_settings():
  env = os.getenv("ENV", "development").lower()

  if env == "production":
    return ProdConfig()
  else:
    return DevConfig()


settings = get_settings()
