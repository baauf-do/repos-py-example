from ultralytics import YOLO
import cv2
from app.utils.decorator_logging import log_execution_time


class YoloDetector:
  def __init__(self, model_path="best.pt"):
    self.model = YOLO(model_path)

  @log_execution_time
  def detect(self, image_path):
    img = cv2.imread(image_path)
    results = self.model(img)
    boxes = []
    for box in results[0].boxes.xyxy:
      boxes.append(tuple(map(int, box.tolist())))
    return boxes
