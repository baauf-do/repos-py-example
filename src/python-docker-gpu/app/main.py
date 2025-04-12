import torch
import tensorflow as tf

print("✅ PyTorch GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "Không có GPU")
print("✅ TensorFlow GPUs:", tf.config.list_physical_devices('GPU'))
