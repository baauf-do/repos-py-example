import os
import requests


def auto_detect_ollama_host():
  """Tự động kiểm tra host hoạt động và trả về host phù hợp"""
  # Ưu tiên từ biến môi trường
  default_host = os.getenv('OLLAMA_HOST', 'host.docker.internal')
  hosts_to_try = [default_host, 'localhost']

  for host in hosts_to_try:
    try:
      response = requests.get(f'http://{host}:11434', timeout=1)
      if response.status_code in [200, 404]:  # 404 vẫn là server phản hồi
        print(f'✅ Kết nối được Ollama tại: {host}')
        return host
    except requests.RequestException:
      print(f'⚠️ Không thể kết nối Ollama tại: {host}')

  raise ConnectionError('❌ Không kết nối được với Ollama ở bất kỳ host nào.')


