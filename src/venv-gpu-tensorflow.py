import tensorflow as tf

tf.debugging.set_log_device_placement(True)
a = tf.constant([[1.0, 2.0, 3.0]])
b = tf.constant([[0.5, 0.5, 0.5]])
c = a + b
print(c)

# Kiểm tra danh sách thiết bị GPU
print("TensorFlow version:", tf.__version__)
print("Built with CUDA:", tf.test.is_built_with_cuda())
print("GPU available:", tf.config.list_physical_devices('GPU'))

# In thông tin chi tiết
for device in tf.config.list_physical_devices('GPU'):
  print(device)
