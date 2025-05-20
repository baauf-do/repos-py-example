import time
from functools import wraps
from app.utils.logging_utils import log_debug

"""Đo thời gian chạy method"""
def log_execution_time(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    duration = (time.time() - start_time) * 1000
    log_debug(f"Executed {func.__name__} in {duration:.2f}ms", level="DEBUG")
    return result

  return wrapper
