# train/eval_all_models.py
from ultralytics import YOLO
from pathlib import Path
import yaml


def evaluate_model(model_path: Path, data_path: str):
  model = YOLO(str(model_path))
  results = model.val(data=data_path)
  return {
    "model": model_path.name,
    "precision": results['precision'],
    "recall": results['recall'],
    "map50": results['map50'],
    "map": results['map'],
  }


def main():
  models_dir = Path("runs")
  data_yaml = "data.yaml"  # Sửa nếu đường dẫn khác
  all_results = []

  for pt_file in models_dir.rglob("*.pt"):
    print(f"🔍 Đánh giá: {pt_file}")
    result = evaluate_model(pt_file, data_yaml)
    all_results.append(result)

  # In kết quả
  print("\n📋 Tổng hợp:")
  for r in all_results:
    print(f"{r['model']:30} | P: {r['precision']:.2f} | R: {r['recall']:.2f} | mAP50: {r['map50']:.2f} | mAP: {r['map']:.2f}")


if __name__ == '__main__':
  main()
