# File: app/services/storage_service.py

from pathlib import Path
from typing import List
from app.utils import file_utils


class StorageService:
  """Dịch vụ quản lý file trong hệ thống."""

  @staticmethod
  def get_upload_folder() -> Path:
    return file_utils.get_store_path("input")

  @staticmethod
  def get_output_folder() -> Path:
    return file_utils.get_store_path("output")

  @staticmethod
  def list_uploaded_files() -> List[str]:
    """Lấy danh sách file trong store/input."""
    upload_folder = StorageService.get_upload_folder()
    return file_utils.list_files_in_folder(upload_folder)

  @staticmethod
  def upload_file(file_path: Path) -> Path:
    """Upload file vào store/input."""
    upload_folder = StorageService.get_upload_folder()
    return file_utils.copy_file(file_path, upload_folder)

  @staticmethod
  def move_to_backup(file_path: Path) -> Path:
    """Di chuyển file vào store/backup."""
    backup_folder = file_utils.get_store_path("backup")
    return file_utils.move_file(file_path, backup_folder)

  @staticmethod
  def delete_uploaded_file(file_name: str) -> bool:
    """Xóa 1 file trong store/input."""
    upload_folder = StorageService.get_upload_folder()
    target_file = upload_folder / file_name
    return file_utils.delete_file(target_file)

  @staticmethod
  def validate_uploaded_pdf(file_name: str) -> Path:
    """Validate file pdf upload."""
    upload_folder = StorageService.get_upload_folder()
    return file_utils.validate_upload_file(file_name, upload_folder)
