import torch
import time

# Kiểm tra xem CUDA có hoạt động không
print("CUDA available:", torch.cuda.is_available())

# In ra tên GPU nếu có
if torch.cuda.is_available():
  print("GPU:", torch.cuda.get_device_name(0))
  print("CUDA Version:", torch.version.cuda)

device = "cuda" if torch.cuda.is_available() else "cpu"

a = torch.rand(10000, 10000, device=device)
b = torch.rand(10000, 10000, device=device)

start = time.time()
c = torch.matmul(a, b)
torch.cuda.synchronize()  # Đảm bảo GPU đã tính xong
end = time.time()

print(f"Thực hiện trên: {device}")
print(f"Thời gian: {end - start:.4f} giây")
