from flask import Flask, render_template, request
import os
import requests
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    file = request.files['file']
    if file:
      filepath = os.path.join(UPLOAD_FOLDER, file.filename)
      file.save(filepath)
      with open(filepath, "rb") as f:
        response = requests.post("http://localhost:8000/extract", files={"file": f})
      text = response.json().get("text", "Không có dữ liệu")
      df = pd.DataFrame({"Nội dung": text.split("\n")})
      return render_template("index.html", table=df.to_html(classes="table table-bordered"))
  return render_template("index.html")
