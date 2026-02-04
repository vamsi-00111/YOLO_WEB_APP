from pathlib import Path

DIR=Path(__file__).parent.absolute()

MODEL_CONFIG={"MODEL_DIR":DIR/"models",
              "PREDICTION_DIR":DIR/"predict"}

LOG_CONFIG={
    "LOG_DIR":DIR/'logs',
    "FILE_LEVEL":"DEBUG",
    "FILE_FORMATTER":"[%(asctime)s] %(levelname)s:%(name)s:%(message)s]"}

TASK_TYPES=["CLASSIFICATION","SEGMENTATION","DETECTION","POSE","OBB","TRACK"]

MODEL_SIZES=["NANO","SMALL","MEDIUM","LARGE","XLARGE"]

MODEL_URLS={
    "CLASSIFICATION":{
        "NANO":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n.pt",
        "SMALL":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26s.pt",
        "MEDIUM":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26m.pt",
        "LARGE":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26l.pt",
        "XLAARGE":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26x.pt"
    },
    "SEGMENTAITION":{
        "NANO":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n.pt",
        "SMALL":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26s.pt",
        "MEDIUM":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26m.pt",
        "LARGE":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26l.pt",
        "XLAARGE":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26x.pt"
    },
    "DETECTION":{
        "NANO":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n.pt",
        "SMALL":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26s.pt",
        "MEDIUM":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26m.pt",
        "LARGE":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26l.pt",
        "XLAARGE":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26x.pt"
    },
    "POSE":{
        "NANO":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n.pt",
        "SMALL":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26s.pt",
        "MEDIUM":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26m.pt",
        "LARGE":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26l.pt",
        "XLAARGE":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26x.pt"
    },
    "OBB":{
        "NANO":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n.pt",
        "SMALL":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26s.pt",
        "MEDIUM":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26m.pt",
        "LARGE":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26l.pt",
        "XLAARGE":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26x.pt"
    },
    "TRACK":{
        "NANO":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n.pt",
        "SMALL":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26s.pt",
        "MEDIUM":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26m.pt",
        "LARGE":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26l.pt",
        "XLAARGE":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26x.pt"
    }
    
}

for directory in [LOG_CONFIG["LOG_DIR"],MODEL_CONFIG["MODEL_DIR"],MODEL_CONFIG["PREDICTION_DIR"]]:
    directory.mkdir(exist_ok=True,parents=True)