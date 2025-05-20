from paddleocr import PaddleOCR
from app.utils.decorator_logging import log_execution_time

class OCRReader:
  def __init__(self):
    self.ocr = PaddleOCR(use_angle_cls=True, lang='en')

  @log_execution_time
  def read(self, image_path):
    result = self.ocr.ocr(image_path)
    texts = []
    for line in result[0]:
      texts.append(line[1][0])
    return " ".join(texts)
