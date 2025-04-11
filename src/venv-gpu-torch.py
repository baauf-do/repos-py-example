import torch

# Kiểm tra xem CUDA có hoạt động không
print("CUDA available:", torch.cuda.is_available())

# In ra tên GPU nếu có
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    print("CUDA Version:", torch.version.cuda)
