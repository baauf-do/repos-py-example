from pdf2image import convert_from_path
import os


def extract_images_from_pdf(pdf_path, output_dir="extracted_images"):
  """
  Trích xuất ảnh từ file PDF và lưu vào thư mục output_dir.
  """
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

  # Convert các trang PDF thành ảnh
  images = convert_from_path(pdf_path)
  image_paths = []

  for idx, image in enumerate(images):
    image_path = os.path.join(output_dir, f"page_{idx + 1}.jpg")
    image.save(image_path, "JPEG")
    image_paths.append(image_path)

  return image_paths
