import os
import subprocess
import sys
import platform
from datetime import datetime

LOG_FILE = "logs/setup.log"


def log(message):
  with open(LOG_FILE, "a", encoding="utf-8") as f:
    f.write(f"{datetime.now()} - {message}\n")
  print(message)


def run(cmd, shell=True):
  log(f"▶ Chạy lệnh: {cmd}")
  result = subprocess.run(cmd, shell=shell)
  if result.returncode != 0:
    log("❌ Có lỗi xảy ra. Dừng lại.")
    sys.exit(result.returncode)


def find_python_versions():
  possible_names = [
    "python", "python3", "py",
    "python3.7", "python3.8", "python3.9", "python3.10", "python3.11", "python3.12",
    "py -3.7", "py -3.8", "py -3.9", "py -3.10", "py -3.11", "py -3.12"
  ]

  found = {}
  for name in possible_names:
    try:
      result = subprocess.run(
        f"{name} --version",
        shell=True,
        capture_output=True,
        text=True
      )
      if result.returncode == 0:
        version = result.stdout.strip() or result.stderr.strip()
        found[name] = version
    except Exception:
      continue
  return found


def load_dotenv(filepath=".env"):
  if not os.path.exists(filepath):
    log("ℹ️ Không tìm thấy file .env")
    return

  log(f"🔵 Đang load file {filepath}:")
  with open(filepath, "r", encoding="utf-8") as f:
    for line in f:
      line = line.strip()
      if line and not line.startswith("#"):
        log(f"   {line}")


def main():
  if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)

  log("=== 🚀 Bắt đầu cài đặt dự án ===")
  versions = find_python_versions()

  if not versions:
    log("❌ Không tìm thấy bản Python nào.")
    sys.exit(1)

  log("🔍 Các phiên bản Python tìm được:")
  for idx, (cmd, version) in enumerate(versions.items(), start=1):
    log(f"  {idx}. {cmd} -> {version}")

  while True:
    try:
      choice = int(input("\n👉 Chọn số tương ứng với phiên bản bạn muốn dùng: "))
      if 1 <= choice <= len(versions):
        break
      else:
        log("⚠️ Lựa chọn không hợp lệ.")
    except ValueError:
      log("⚠️ Nhập một số nguyên.")

  selected_cmd = list(versions.keys())[choice - 1]

  log(f"\n✅ Sử dụng Python: {selected_cmd}")

  # Tên thư mục môi trường ảo
  venv_dir = ".venv-green"

  # Kiểm tra xem môi trường ảo đã tồn tại chưa
  if not os.path.exists(venv_dir):
    log("\n📦 Tạo môi trường ảo...")
    run(f"{selected_cmd} -m venv {venv_dir}")
  else:
    log("\n🔄 Môi trường ảo đã tồn tại, bỏ qua bước tạo mới môi trường.")

  # Xác định hệ điều hành
  is_windows = platform.system() == "Windows"

  # Đường dẫn python & pip trong môi trường ảo
  python_in_venv = os.path.join(venv_dir, "Scripts" if is_windows else "bin", "python")
  pip_exec = os.path.join(venv_dir, "Scripts" if is_windows else "bin", "pip")

  # Nâng cấp pip đúng cách
  log("\n⬆️ Nâng cấp pip...")
  run([python_in_venv, "-m", "pip", "install", "--upgrade", "pip"])

  # Cài đặt requirements nếu có
  if os.path.exists("requirements.txt"):
    log("\n📚 Cài đặt hoặc cập nhật requirements.txt...")
    run([pip_exec, "install", "--upgrade", "-r", "requirements.txt"])
  else:
    log("⚠️ Không tìm thấy file requirements.txt, bỏ qua bước cài đặt thư viện.")

  # Cài đặt Jupyter và ipykernel
  log("\n📦 Cài đặt Jupyter và ipykernel để sử dụng môi trường ảo trong Jupyter Notebook...")
  run([pip_exec, "install", "jupyter", "ipykernel"])

  # Đăng ký môi trường ảo làm kernel cho Jupyter
  log("\n🔧 Đăng ký môi trường ảo làm kernel cho Jupyter...")
  run([python_in_venv, "-m", "ipykernel", "install", "--user", f"--name={venv_dir}", "--display-name", f"Python ({venv_dir})"])

  # Load biến môi trường nếu có
  load_dotenv()

  # Hướng dẫn kích hoạt
  activate_cmd = (
    f"{venv_dir}\\Scripts\\activate" if is_windows else f"source {venv_dir}/bin/activate"
  )

  log("\n✅ Hoàn tất cài đặt!")
  log(f"\n👉 Để kích hoạt môi trường ảo, chạy:\n{activate_cmd}")
  log(f"\n📝 File log cài đặt đã lưu ở: {LOG_FILE}")


if __name__ == "__main__":
  main()
