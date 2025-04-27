import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()  # Load biến môi trường từ file .env

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
  uvicorn.run(
    "app.main:app",
    host=HOST,
    port=PORT,
    reload=True
  )
