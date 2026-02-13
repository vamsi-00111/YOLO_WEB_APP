from flask import Flask, render_template, request
import numpy as np
import cv2
from yolo import YoloDetecter

app = Flask(__name__)
application=app
model = YoloDetecter()


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/detect", methods=["POST"])
def detect():

    if "image" not in request.files:
        return "No file uploaded"

    file = request.files["image"]

    if file.filename == "":
        return "No selected file"

    # Convert uploaded image to numpy
    file_bytes = file.read()
    np_arr = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # detect() saves image in static/result/uuid.jpg
    filename = model.detect(img)   # returns "uuid.jpg"

    return render_template(
        "detect.html",
        prediction=f"result/{filename}"
    )


if __name__ == "__main__":
    app.run(debug=True)
