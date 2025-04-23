# train/train.py
from ultralytics import YOLO
from pathlib import Path
from datetime import datetime
import argparse
import yaml
import matplotlib.pyplot as plt

# ---------- Cấu hình mặc định ----------
DEFAULT_MODEL = 'yolov8n.pt'
DEFAULT_DATASET = str(Path(__file__).parent / 'data.yaml')
DEFAULT_EPOCHS = 100
DEFAULT_IMGSZ = 640
DEFAULT_BATCH = 16
DEFAULT_LR = 0.001


def plot_metrics_bar(metrics_dict, save_path):
  keys = ['precision', 'recall', 'map50', 'map']
  values = [getattr(metrics_dict, k) for k in keys]

  plt.figure(figsize=(8, 5))
  plt.bar(keys, values)
  plt.ylabel('Score')
  plt.title('📊 Evaluation Metrics')
  for i, v in enumerate(values):
    plt.text(i, v + 0.01, f'{v:.2f}', ha='center')
  plt.tight_layout()
  plt.savefig(save_path / 'metrics_bar.png')
  plt.close()


# ---------- Hàm huấn luyện ----------
def train_yolov8_model(model_path: str, data_path: str, epochs: int, imgsz: int, batch: int, run_name: str, lr0: float = 0.01):
  """
  Huấn luyện mô hình YOLOv8 và ghi log, đánh giá sau huấn luyện.
  """
  save_path = Path('runs')
  save_path.mkdir(exist_ok=True)
  run_path = save_path / run_name

  # Load và train model
  model = YOLO(model_path)
  model.train(data=data_path, epochs=epochs, imgsz=imgsz, batch=batch, project=str(save_path), name=run_name, lr0=lr0)

  # ---------- Ghi log thông số ----------
  log_file = run_path / 'train_log.txt'
  with open(log_file, 'w') as f:
    f.write(f'Model: {model_path}\n')
    f.write(f'Dataset: {data_path}\n')
    f.write(f'Epochs: {epochs}\n')
    f.write(f'Image size: {imgsz}\n')
    f.write(f'Batch size: {batch}\n')
    f.write(f'Learning rate: {lr0}\n')

  print(f'✅ Huấn luyện xong. Kết quả tại: {run_path}')

  # ---------- Đánh giá mô hình ----------
  metrics = model.val(data=data_path)
  plot_metrics_bar(metrics, run_path)
  print('📊 Kết quả đánh giá:')
  for k, v in metrics.items():
    print(f'{k}: {v}')

  # Ghi kết quả đánh giá vào log
  with open(log_file, 'a') as f:
    f.write('\n[Evaluation metrics]\n')
    for k, v in metrics.items():
      f.write(f'{k}: {v}\n')


# ---------- CLI Entry Point ----------
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Train YOLOv8 model with custom options')
  parser.add_argument('--model', type=str, default=DEFAULT_MODEL, help='YOLO model path or name')
  parser.add_argument('--data', type=str, default=DEFAULT_DATASET, help='Path to data.yaml')
  parser.add_argument('--epochs', type=int, default=DEFAULT_EPOCHS, help='Number of training epochs')
  parser.add_argument('--imgsz', type=int, default=DEFAULT_IMGSZ, help='Image size')
  parser.add_argument('--batch', type=int, default=DEFAULT_BATCH, help='Batch size')
  parser.add_argument('--lr', type=float, default=DEFAULT_LR, help='Learning rate')
  parser.add_argument('--run_name', type=str, default=f'passport_{datetime.now().strftime("%Y%m%d_%H%M%S")}', help='Run name (output folder name)')

  args = parser.parse_args()

  train_yolov8_model(
    model_path=args.model, data_path=args.data, epochs=args.epochs, imgsz=args.imgsz, batch=args.batch, run_name=args.run_name, lr0=args.lr
  )
