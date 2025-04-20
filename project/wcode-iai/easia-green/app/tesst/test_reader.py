# app/test/test_reader.py
import os
from core.reader import extract_passport_info

INPUT_PATH = "store/input/sample-passport.jpg"

def test_extract_passport_info():
    if not os.path.exists(INPUT_PATH):
        print("⚠️  File test không tồn tại:", INPUT_PATH)
        return

    with open(INPUT_PATH, "rb") as f:
        file_bytes = f.read()

    try:
        result = extract_passport_info("sample-passport.jpg", file_bytes)
        print("✅ Trích xuất thành công:")
        for k, v in result.items():
            print(f"{k}: {v}")
    except Exception as e:
        print("❌ Lỗi trích xuất:", str(e))

if __name__ == "__main__":
    test_extract_passport_info()
