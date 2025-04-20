# run_tests.py
import subprocess
import sys

print("\n🧪 Đang chạy toàn bộ test trong thư mục app/test/...\n")

result = subprocess.run([
  sys.executable, "-m", "pytest", "app/test", "-v", "--tb=short"
])

if result.returncode == 0:
  print("\n✅ Tất cả test đều chạy thành công!")
else:
  print("\n❌ Một số test bị lỗi. Vui lòng kiểm tra lại chi tiết bên trên.")

sys.exit(result.returncode)
