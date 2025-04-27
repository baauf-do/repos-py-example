from fastapi import FastAPI
import os
from app.services.pdf_processor import PDFProcessor
from app.models.export_utils import text_to_dataframe, export_to_json, export_to_excel
from datetime import datetime
from fastapi.responses import JSONResponse

dtnow = datetime.now()

app = FastAPI()


@app.get("/")
def read_root():
  return {"message": "Hello World"}


@app.post("/process-pdf/")
def process_pdfs():
  input_dir = "store/input"
  output_dir = "store/output"
  temp_dir = "store/temp"

  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  processor = PDFProcessor(input_dir, temp_dir)

  results = []
  for file_name in os.listdir(input_dir):
    if file_name.endswith(".pdf"):
      pdf_path = os.path.join(input_dir, file_name)
      print(f"Đang xử lý file: {file_name}")

      method = "text"  # or "image"
      text = processor.process_pdf(pdf_path, method=method)

      df = text_to_dataframe(text)

      json_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}-{dtnow.strftime('%Y%m%d%H%M%S')}.json")
      excel_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}-{dtnow.strftime('%Y%m%d%H%M%S')}.xlsx")
      export_to_json(df, json_path)
      export_to_excel(df, excel_path)

      results.append({
        "file": file_name,
        "json_output": json_path,
        "excel_output": excel_path
      })

  return JSONResponse(content={"results": results})
