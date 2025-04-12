# D:\Projects\ai-test\hello_gpu.py
import torch

print("Có GPU không?", torch.cuda.is_available())
print("Tên GPU:", torch.cuda.get_device_name(0))
