#!/bin/bash

# ✅ Kiểm tra xem model đã tồn tại chưa
if ! ollama list | grep -q "llama3.2"; then
  echo "📥 Pulling llama3.2 model..."`
  #ollama pull llama3.2
  ollama ollama run llama3.2
else
  echo "✅ llama3.2 model already exists."
fi

# 🎯 Serve sau khi pull
ollama serve
