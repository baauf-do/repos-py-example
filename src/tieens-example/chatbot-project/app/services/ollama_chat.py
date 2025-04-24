import os
import requests
from app.utils.ollama_client import auto_detect_ollama_host


def call_ollama_chat(message: str, model: str = 'llama3.2'):
  get_host = auto_detect_ollama_host()  # Tự động phát hiện host
  # Nếu không có biến môi trường OLLAMA_HOST, sẽ dùng localhost mặc định
  host = os.getenv('OLLAMA_HOST', get_host)  # 👈 Dùng IP cầu nối đến máy thật
  url = f'http://{host}:11434/api/generate'
  payload = {'model': model, 'prompt': message, 'stream': False}

  try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
      return response.json().get('response', '')
    else:
      return f'❌ Error: {response.status_code} - {response.text}'
  except Exception as e:
    return f'❌ Lỗi khi gọi Ollama: {str(e)}'
