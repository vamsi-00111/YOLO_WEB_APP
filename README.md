# 🚀 YOLO Web App

A Computer Vision application built with **YOLO, FastAPI, Streamlit, OpenCV, and Python** for performing **Object Detection** and **Instance Segmentation** on images.

The application provides both:

* 🌐 A **Streamlit Web Interface** for interactive usage
* ⚡ A **FastAPI REST API** for programmatic access

---

## ✨ Features

* 🔍 Object Detection using YOLO models
* 🎯 Instance Segmentation
* 📦 Multiple Model Sizes

  * Nano
  * Small
  * Medium
* 🖥️ CPU & GPU Inference Support
* ⚡ FastAPI Backend
* 🎨 Streamlit Frontend
* 📊 Configurable Detection Parameters
* 📝 Logging Support

---

## 📂 Project Structure

```text
YOLO_WEB_APP/
│
├── fast_api.py          # FastAPI backend
├── streamlit.py         # Streamlit frontend
├── yolo.py              # Detection & segmentation logic
├── config.py            # Application configuration
├── logger.py            # Logging utility
├── requirements.txt
├── .gitignore
│
├── models/              # YOLO model weights (ignored by Git)
├── logs/                # Log files
│
├── image.png            # Sample image
├── dog.webp             # Sample image
└── test.ipynb           # Development notebook
```

---
## 🛠️ Installation

### Clone the Repository

```bash
git clone https://github.com/vamsi-00111/YOLO_WEB_APP.git
cd YOLO_WEB_APP
```

### Create Conda Environment

```bash
conda create -n YoloApp python=3.12
conda activate YoloApp
```

### Install Dependencies

```bash
pip install -r requirements.txt
```


---

## 🤖 Model Management

The application automatically manages model weights.

When a model is selected for the first time:

1. The `models/` directory is created automatically.
2. Required YOLO weights are downloaded automatically.
3. Downloaded weights are cached locally for future use.

Example:

```text
models/
├── yolo26n_DETECTION.pt
├── yolo26s_DETECTION.pt
├── yolo26m_DETECTION.pt
├── yolo26n_SEGMENTATION.pt
├── yolo26s_SEGMENTATION.pt
└── yolo26m_SEGMENTATION.pt
```

> Note: Model files are not tracked by Git and are excluded through `.gitignore`.


---

## 🚀 Running the Streamlit App

```bash
streamlit run streamlit.py
```

Open:

```text
http://localhost:8501
```

---

## ⚡ Running the FastAPI Server

```bash
uvicorn fast_api:app --reload
```

Open API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

### 📡 API Endpoints

### Object Detection

```http
POST /detect
```

Performs object detection on the uploaded image and returns the processed image with bounding boxes drawn around detected objects.

#### Parameters

| Parameter  | Type       | Description         |
| ---------- | ---------- | ------------------- |
| file       | Image File | Input image         |
| model_size | String     | NANO, SMALL, MEDIUM |
| device     | String     | cpu or cuda         |

#### Response

* Annotated image (JPEG format)
* Bounding boxes rendered on detected objects

---

## Instance Segmentation

```http
POST /segment
```

Performs instance segmentation on the uploaded image and returns the processed image with segmentation masks rendered.

#### Parameters

| Parameter  | Type       | Description         |
| ---------- | ---------- | ------------------- |
| file       | Image File | Input image         |
| model_size | String     | NANO, SMALL, MEDIUM |
| device     | String     | cpu or cuda         |

#### Response

* Annotated image (JPEG format)
* Segmentation masks rendered on detected objects

---

## 🖼️ Example Workflow

1. Upload an image.
2. Select:

   * Detection or Segmentation
   * Model Size
   * Device (CPU/GPU)
3. Run inference.
4. View the processed output image.

---

## 🧰 Technologies Used

* Python
* FastAPI
* Streamlit
* OpenCV
* NumPy
* Ultralytics YOLO

---

## 🔮 Future Improvements

* Video Processing Support
* Real-time Webcam Inference
* Batch Image Processing
* Model Benchmark Dashboard
* Docker Deployment
* Cloud Deployment

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Vamsi**

If you find this project useful, feel free to star the repository and contribute.
