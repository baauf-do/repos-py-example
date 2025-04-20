# train/train.py
from ultralytics import YOLO
from pathlib import Path

# Cấu hình mặc định
DEFAULT_MODEL = "yolov8n.pt"  # Có thể thay bằng yolov8s.pt nếu muốn chính xác hơn
DEFAULT_DATASET = "mrz.yaml"
DEFAULT_EPOCHS = 100
DEFAULT_IMGSZ = 640
DEFAULT_BATCH = 16


def train_yolov8_model(
  model_path: str = DEFAULT_MODEL,
  data_path: str = DEFAULT_DATASET,
  epochs: int = DEFAULT_EPOCHS,
  imgsz: int = DEFAULT_IMGSZ,
  batch: int = DEFAULT_BATCH,
  run_name: str = "mrz"
):
  """
  Huấn luyện mô hình YOLOv8 cho nhận diện vùng MRZ
  """
  save_path = Path("runs")
  save_path.mkdir(exist_ok=True)

  model = YOLO(model_path)
  model.train(
    data=data_path,
    epochs=epochs,
    imgsz=imgsz,
    batch=batch,
    project=str(save_path),
    name=run_name
  )

  print(f"✅ Đã huấn luyện xong. Kết quả lưu tại: {save_path / run_name}")


if __name__ == "__main__":
  train_yolov8_model()
