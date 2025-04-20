_model_cache = {}


def load_yolo_model(path: str = "app/models/yolov8_mrz.pt") -> YOLO:
  """
  Load mô hình YOLO từ file, sử dụng cache nếu đã load trước đó.
  """
  if path in _model_cache:
    log_debug(f"📦 [Model] Dùng lại mô hình từ cache: {path}", level="DEBUG")
    return _model_cache[path]

  try:
    model = YOLO(path)
    _model_cache[path] = model
    log_debug(f"✅ [Model] Đã load mô hình YOLO: {path}", level="INFO")
    return model
  except Exception as e:
    log_debug(f"❌ [Model] Lỗi khi load mô hình YOLO: {e}", level="ERROR")
    return None
