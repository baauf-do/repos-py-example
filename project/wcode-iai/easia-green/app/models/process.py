import cv2
import paddleocr
from passporteye import read_mrz
import json


def extract_mrz_info(image_path):
  """
  Hàm này sử dụng PassportEye để nhận diện MRZ từ ảnh hộ chiếu và trả về thông tin dạng dictionary.
  """
  mrz = read_mrz(image_path)
  if mrz is not None:
    return mrz.to_dict()
  else:
    return {"error": "MRZ not found"}


def preprocess_image(image_path):
  """
  Hàm này dùng OpenCV để chuyển ảnh sang ảnh xám và áp dụng thresholding để làm rõ các ký tự.
  """
  image = cv2.imread(image_path)
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Chuyển sang ảnh xám
  _, thresh_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)  # Áp dụng thresholding
  return thresh_image


def extract_text_from_image(image):
  """
  Hàm này sử dụng PaddleOCR để nhận diện văn bản từ ảnh.
  """
  ocr = paddleocr.OCR(use_angle_cls=True, lang='en')  # Sử dụng ngôn ngữ tiếng Anh
  result = ocr.ocr(image, cls=True)  # Nhận diện văn bản
  return result


def parse_passport(image_path):
  """
  Hàm kết hợp các bước trên để trích xuất thông tin từ ảnh passport.
  Trả về kết quả MRZ và văn bản OCR dưới dạng JSON.
  """
  # Trích xuất MRZ
  mrz_info = extract_mrz_info(image_path)

  # Xử lý ảnh với OpenCV
  processed_image = preprocess_image(image_path)

  # Trích xuất văn bản với PaddleOCR
  ocr_result = extract_text_from_image(processed_image)

  # Tạo kết quả trả về dưới dạng JSON
  structured_data = {
    "mrz_info": mrz_info,
    "ocr_result": ocr_result
  }

  return json.dumps(structured_data, ensure_ascii=False, indent=4)
