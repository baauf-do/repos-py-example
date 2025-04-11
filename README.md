# repos-py-example
Learn python through examples

## 1. Author
- [baauf](https://github.com/domanhcuong2707)

## 2. Technical

- Python 3.12.4
- Jupyter

- ide
  - vscode
  - import file for vscode [ide-vscode-py](https://github.com/baauf-do/repos-py-example/blob/main/sources/ide/ide-vscode-py.code-profile)

## 3. Setup

- read [setup.md](https://github.com/baauf-do/repos-py-example/blob/main/sources/document/setup.md) file in folder source/document

## 4.Content

- in folder: [src](https://github.com/baauf-do/repos-py-example/tree/main/src)
  - 1. [days-of-python](https://github.com/baauf-do/repos-py-example/tree/main/src/days-of-python)
  - 2. [example](https://github.com/baauf-do/repos-py-example/tree/main/src/example)


## ... Reference
- [installing-using-pip-and-virtual-environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

# Them moi truong su dung dc GPU
- su dung cac thu vien lien quan toi
  - OCR AI 👉 Dùng PyTorch hoặc TensorFlow trên GPU.
  - OCR Tesseract 👉 Bật OpenCL nếu có.
  - Xử lý ảnh PDF 👉 Dùng multiprocessing hoặc Pillow-SIMD.
  - ...
- yeu cau phai co card do hoa (vd: rtx4060)
  - cap nhat drive card
  - tai ve cai dat 2 cai
    - Tải & Cài đặt CUDA 12.8
    - Tải & Cài đặt cuDNN 9.8.0 cho CUDA 12.8
      - cuDNN 9.8.0
      - CUDA 12.x
      - Windows x86_64
  - kiem tra xem da co CUDA chua
  ```bash
  nvcc --version
  ```
  - kiem tra cdDNN, bang cach kiem tra file da ton tai chua
  ```bash
  C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.3\bin\cudnn64_8.dll
  ```
- Step by step
  - them moi truong
  - truoc tien phai cai dat duoc python phien ban 3.11.x
  - sau do chay
  ```bash
  py -3.11 -m venv venv311
  ```
- truy cap vao venv
```pwsh
venv311\Scripts\activate
```
- thoat khoi
```pwsh
deactivate
```
- update pip truoc khi cai dat
```pwsh
py -m pip install --upgrade pip
```
- cai dat cac thu vien can thiet
  - Cài TensorFlow GPU va test
  ```pwsh
  pip install tensorflow==2.15.0

  py src/venv-gpu-tensorflow.py
  ```
  - Cài PyTorch GPU va test
  ```pwsh
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

  py src/venv-gpu-torch.py
  ```


- chay test thu
```py
import torch
import pytesseract
from pdf2image import convert_from_path

# Kiểm tra GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

# Đọc PDF thành ảnh
images = convert_from_path("sample.pdf", dpi=300)

# Chạy OCR trên từng trang
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image)
    print(f"Page {i+1}:", text)
```
