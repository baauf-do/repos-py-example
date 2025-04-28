from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import time
from app.utils.logging_utils import log_debug


class LoggingMiddleware(BaseHTTPMiddleware):
  async def dispatch(self, request: Request, call_next):
    start_time = time.time()

    log_debug(f"Request: {request.method} {request.url.path}", level="INFO")

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    log_debug(
      f"Response: {request.method} {request.url.path} - Status {response.status_code} - {process_time:.2f}ms",
      level="INFO"
    )

    return response
