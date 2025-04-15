from fastapi import FastAPI, UploadFile, File
from services.pdf_parser import extract_pdf_text
from models.contract import Contract

app = FastAPI()

# Định nghĩa endpoint để nhận file PDF và trả về văn bản trích xuất
@app.post("/extract_pdf/")
async def extract_pdf(file: UploadFile = File(...)):
  # Gọi dịch vụ để trích xuất văn bản từ file PDF
  contract_text = extract_pdf_text(file.file)

  # Tạo đối tượng hợp đồng (có thể lưu vào cơ sở dữ liệu nếu cần)
  contract = Contract(contract_text=contract_text)

  return {"extracted_text": contract.contract_text}

# Định nghĩa endpoint để kiểm tra xem ứng dụng đang chạy
@app.get("/")
async def root():
    return {"message": "Hello World"}
