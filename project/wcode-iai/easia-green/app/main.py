# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import endpoints

app = FastAPI(title="easia-green | Passport OCR + MRZ Reader")

# Cho phép CORS nếu tích hợp web/app khác
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# Gắn các router từ endpoints
app.include_router(endpoints.router)


@app.get("/")
def read_root():
  return {"message": "easia-green API is running 🚀"}
