from fastapi import FastAPI, File, UploadFile
from app.services.passport_parser import parse_passport
from app.services.pdf_image_parser import extract_images_from_pdf
import json
from app.services.log_run import log

app = FastAPI()


@app.post("/extract-passport-data/")
async def extract_passport_data(file: UploadFile = File(...)):
  """
  Endpoint nhận ảnh passport, xử lý và trả về thông tin MRZ và văn bản từ ảnh.
  """
  # Lưu ảnh passport tạm thời
  log("Start processing passport image")
  try:
    log("Start saving image")
    # lấy tên file từ header
    filename = file.filename
    image_path = f"temp/temp_{filename}.jpg"
    with open(image_path, "wb") as buffer:
      buffer.write(await file.read())
    log("Image saved successfully")
  except Exception as e:
    log(f"Error saving image: {e}")
    return {"error": "Failed to save image"}

  # Xử lý passport và trả về thông tin
  result = parse_passport(image_path)
  return json.loads(result)


@app.post("/extract-pdf-passport-data/")
async def extract_pdf_passport_data(file: UploadFile = File(...)):
  """
  Endpoint nhận file PDF chứa ảnh passport, trích xuất ảnh và xử lý các ảnh.
  """
  # Lưu file PDF tạm thời
  pdf_path = "temp_passport.pdf"
  with open(pdf_path, "wb") as buffer:
    buffer.write(await file.read())

  # Trích xuất ảnh từ PDF
  image_paths = extract_images_from_pdf(pdf_path)

  # Xử lý các ảnh và trả về kết quả
  result = []
  for image_path in image_paths:
    passport_data = parse_passport(image_path)
    result.append(json.loads(passport_data))

  return result
