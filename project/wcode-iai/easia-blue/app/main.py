from fastapi import FastAPI
from app.api.endpoints import upload, extract, database, status, files, process_pdf
from app.utils.logging_utils import configure_logging
from app.utils.middleware_logging import LoggingMiddleware

logger = configure_logging()

app = FastAPI(title="easia-blue Contract Extraction API")

# Thêm middleware log
app.add_middleware(LoggingMiddleware)

# Include routers
app.include_router(upload.router, prefix="/api")
app.include_router(extract.router, prefix="/api")
app.include_router(database.router, prefix="/api")
app.include_router(status.router, prefix="/api")
app.include_router(files.router, prefix="/api")
app.include_router(process_pdf.router, prefix="/api")


@app.get("/")
async def root():
  return {"message": "Welcome to the easia-blue Contract Extraction API!"}
