from fastapi import APIRouter, Body
from app.services.ollama_chat import call_ollama_chat
# from app.services.data_loader import load_excel_data
# from app.core.config import EXCEL_PATH

router = APIRouter()


@router.post('/chat')
def chat_with_bot(message: str = Body(..., embed=True)):
  #data = load_excel_data(EXCEL_PATH)
  # Bạn có thể xử lý thêm logic tìm thông tin liên quan trong data ở đây
  # data = data.to_dict(orient='records')
  reply = call_ollama_chat(message)
  return {'reply': reply}


