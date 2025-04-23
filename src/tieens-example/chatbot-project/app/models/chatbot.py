import os
import requests


def call_ollama_chat(message: str, model: str = 'llama3'):
  host = os.getenv('OLLAMA_HOST', 'host.docker.internal')  # 👈 Dùng IP cầu nối đến máy thật
  url = f'http://{host}:11434/api/generate'
  payload = {'model': model, 'prompt': message, 'stream': False}

  try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
      return response.json().get('response', '')
    else:
      return f'Error: {response.status_code} - {response.text}'
  except Exception as e:
    return f'Request failed: {str(e)}'
