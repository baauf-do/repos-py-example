import datetime
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.services.pdf_parser import parse_contract
# import uvicorn

app = FastAPI(title="EASIA Contract Extractor API", description="Trích xuất thông tin hợp đồng từ file PDF")

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


@app.post("/extract-contract")
async def extract_contract(file: UploadFile = File(...)):
  if not file.filename.lower().endswith(".pdf") or file.content_type != "application/pdf":
    raise HTTPException(status_code=400, detail="File không hợp lệ. Vui lòng upload file PDF.")

  content = await file.read()
  try:
    result = parse_contract(content)
    return JSONResponse(content=result)
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Lỗi xử lý file: {str(e)}")


# Định nghĩa endpoint để kiểm tra xem ứng dụng đang chạy
@app.get('/')
def root():
  t = datetime.datetime.now()
  return {'Welcome to Easia-Red PDF Extractor - ': t}


# if __name__ == '__main__':
#   uvicorn.run(app, host='127.0.0.1', port=8085, log_level='info')
