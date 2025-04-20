import tempfile
from pdf2image import convert_from_bytes
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='vi', use_gpu=False)


def extract_text_from_pdf(file_bytes):
  result_text = []
  with tempfile.TemporaryDirectory() as temp_dir:
    images = convert_from_bytes(file_bytes)
    for img in images:
      temp_path = f"{temp_dir}/temp.jpg"
      img.save(temp_path)
      result = ocr.ocr(temp_path, cls=True)
      page_text = [box[1][0] for line in result for box in line]
      result_text.append(" ".join(page_text))

  return {"text": "\n".join(result_text)}
