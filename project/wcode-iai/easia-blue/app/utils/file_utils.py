from pathlib import Path
from typing import List
import shutil
from app.utils.logging_utils import log_debug


# ------------------------
# Kiểm tra file và thư mục
# ------------------------

def file_exists(file_path: Path) -> bool:
  """Kiểm tra file có tồn tại không."""
  exists = file_path.is_file()
  log_debug(f"Check file exists: {file_path} -> {exists}", level="DEBUG")
  return exists


def is_valid_extension(file_name: str, allowed_extensions: List[str] = None) -> bool:
  """Kiểm tra file có đúng đuôi mở rộng (.pdf, .json) không."""
  if allowed_extensions is None:
    allowed_extensions = ['.pdf', '.json']

  ext = Path(file_name).suffix.lower()
  is_valid = ext in allowed_extensions
  log_debug(f"Check file extension: {file_name} -> {is_valid}", level="DEBUG")
  return is_valid


def create_folder(path: Path):
  """Tạo thư mục nếu chưa tồn tại."""
  path.mkdir(parents=True, exist_ok=True)
  log_debug(f"Created folder: {path}", level="DEBUG")


# ------------------------
# Di chuyển và xử lý file
# ------------------------

def move_file(source_path: Path, dest_folder: Path) -> Path:
  """Di chuyển file từ source tới thư mục đích."""
  create_folder(dest_folder)
  dest_path = dest_folder / source_path.name
  shutil.move(str(source_path), str(dest_path))
  log_debug(f"Moved file from {source_path} to {dest_path}", level="INFO")
  return dest_path


def copy_file(source_path: Path, dest_folder: Path) -> Path:
  """Copy file từ source tới thư mục đích."""
  create_folder(dest_folder)
  dest_path = dest_folder / source_path.name
  shutil.copy2(str(source_path), str(dest_path))
  log_debug(f"Copied file from {source_path} to {dest_path}", level="INFO")
  return dest_path


# ------------------------
# Validate trước khi xử lý
# ------------------------

def validate_upload_file(file_name: str, upload_folder: Path) -> Path:
  """
  Validate file upload: tồn tại + đúng extension + đúng folder.
  Trả về đường dẫn đầy đủ nếu hợp lệ.
  """
  file_path = upload_folder / file_name

  if not file_exists(file_path):
    raise FileNotFoundError(f"File {file_name} không tồn tại trong {upload_folder}")

  if not is_valid_extension(file_name, allowed_extensions=['.pdf']):
    raise ValueError(f"File {file_name} không phải định dạng PDF hợp lệ")

  log_debug(f"Validated uploaded file: {file_name}", level="INFO")
  return file_path


# ------------------------
# Tiện ích bổ sung
# ------------------------

def delete_file(file_path: Path) -> bool:
  """Xóa file nếu tồn tại."""
  if file_path.exists() and file_path.is_file():
    file_path.unlink()
    log_debug(f"Deleted file: {file_path}", level="INFO")
    return True
  else:
    log_debug(f"File not found to delete: {file_path}", level="WARNING")
    return False


def list_files_in_folder(folder_path: Path) -> List[str]:
  """Lấy danh sách tất cả file trong thư mục."""
  if not folder_path.exists() or not folder_path.is_dir():
    return []
  return [f.name for f in folder_path.iterdir() if f.is_file()]


def get_store_path(sub_folder: str = "") -> Path:
  """
  Lấy đường dẫn tuyệt đối tới thư mục store + subfolder
  """
  base_dir = Path(__file__).resolve().parent.parent.parent
  store_dir = base_dir / "store"
  full_path = store_dir / sub_folder
  create_folder(full_path)
  return full_path
