from app.utils.decorator_logging import log_execution_time
import pdfplumber
from pdf2image import convert_from_path
import os


class PDFProcessor:
  @staticmethod
  @log_execution_time
  def check_pdf_type(pdf_path: str) -> str:
    with pdfplumber.open(pdf_path) as pdf:
      has_text, has_image = False, False
      for page in pdf.pages:
        if page.extract_text():
          has_text = True
        else:
          has_image = True
    if has_text and not has_image:
      return "text"
    elif has_image and not has_text:
      return "scan"
    else:
      return "mixed"

  @staticmethod
  @log_execution_time
  def pdf_to_images(pdf_path: str, output_folder: str):
    images = convert_from_path(pdf_path)
    image_paths = []
    for i, img in enumerate(images):
      img_path = os.path.join(output_folder, f"page_{i}.png")
      img.save(img_path, "PNG")
      image_paths.append(img_path)
    return image_paths
