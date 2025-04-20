from datetime import datetime
import os

LOG_FILE = os.path.join(os.getcwd(), "..", f"logs/run-fastapi-{datetime.now().strftime('%Y%m%d%H%M%S')}.log")


def log(message):
  with open(LOG_FILE, "a", encoding="utf-8") as f:
    f.write(f"{datetime.now()} - {message}\n")
  print(message)


def log_function(message):
  print(f"Log message: {message}")
