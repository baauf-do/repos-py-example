import re


def clean_text(text: str) -> str:
  # Loại bỏ ký tự đặc biệt không mong muốn
  text = text.replace('\n', ' ')  # bỏ xuống dòng
  text = text.replace('\t', ' ')  # bỏ tab
  text = text.replace('\x0c', '')  # bỏ ký tự ngắt trang (common trong pdf)

  # Loại bỏ các ký tự không phải chữ, số, dấu câu cơ bản (nếu muốn mạnh tay hơn)
  text = re.sub(r'[^\w\s.,;:!?()\[\]\'"-]', '', text)

  # Chuẩn hóa lại khoảng trắng (nhiều space về 1)
  text = re.sub(r'\s+', ' ', text).strip()

  return text
