import os
import pdfplumber
from pdf2image import convert_from_path
from paddleocr import PaddleOCR
import pandas as pd
from concurrent.futures import ThreadPoolExecutor


def read_pdf_to_text(pdf_path):
  """
  Đọc trực tiếp văn bản từ file PDF.
  :param pdf_path: Đường dẫn đến file PDF.
  :return: Chuỗi văn bản trích xuất.
  """
  text_data = []
  with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
      text = page.extract_text()
      if text:
        text_data.append(text)
  return "\n".join(text_data)


class PDFProcessor:
  def __init__(self, temp_dir, use_gpu=False):
    self.temp_dir = temp_dir
    self.ocr = PaddleOCR(use_angle_cls=True, lang="vi", use_gpu=use_gpu)  # Sử dụng GPU nếu có
    if not os.path.exists(temp_dir):
      os.makedirs(temp_dir)

  def read_pdf_to_images(self, pdf_path):
    """
    Chuyển từng trang PDF thành hình ảnh.
    :param pdf_path: Đường dẫn đến file PDF.
    :return: Danh sách đường dẫn đến các file hình ảnh.
    """
    images = convert_from_path(pdf_path, dpi=250, output_folder=self.temp_dir, fmt="png")
    image_paths = []
    for i, image in enumerate(images):
      image_path = os.path.join(self.temp_dir, f"page_{i + 1}.png")
      image.save(image_path, "PNG")
      image_paths.append(image_path)
    return image_paths

  def ocr_images_to_text(self, image_paths):
    """
    Sử dụng OCR để trích xuất văn bản từ danh sách hình ảnh.
    :param image_paths: Danh sách đường dẫn đến các file hình ảnh.
    :return: Chuỗi văn bản trích xuất.
    """
    text_data = []
    for image_path in image_paths:
      result = self.ocr.ocr(image_path, cls=True)
      for line in result[0]:
        text_data.append(line[1][0])  # Lấy nội dung văn bản
      os.remove(image_path)  # Xóa file ảnh ngay sau khi xử lý
    return "\n".join(text_data)

  def process_pdf(self, pdf_path, method="text"):
    """
    Xử lý file PDF theo phương pháp chỉ định.
    :param pdf_path: Đường dẫn đến file PDF.
    :param method: "text" để đọc trực tiếp, "image" để đọc qua hình ảnh.
    :return: Chuỗi văn bản trích xuất.
    """
    if method == "text":
      return read_pdf_to_text(pdf_path)
    elif method == "image":
      image_paths = self.read_pdf_to_images(pdf_path)
      return self.ocr_images_to_text(image_paths)
    else:
      raise ValueError("Phương pháp không hợp lệ. Chọn 'text' hoặc 'image'.")

  def process_pdfs_parallel(self, pdf_paths, method="text", max_workers=2):
    """
    Xử lý nhiều file PDF song song.
    :param pdf_paths: Danh sách đường dẫn đến các file PDF.
    :param method: "text" hoặc "image".
    :param max_workers: Số luồng xử lý song song.
    :return: Danh sách kết quả xử lý.
    """
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
      results = list(executor.map(lambda pdf: self.process_pdf(pdf, method), pdf_paths))
    return results
