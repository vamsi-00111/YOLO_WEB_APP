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

    "DETECTION":{
        "NANO":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n.pt",
        "SMALL":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26s.pt",
        "MEDIUM":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26m.pt",
        "LARGE":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26l.pt",
        "XLAARGE":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26x.pt"
    },
    "SEGMENTATION":{
        "NANO":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n-seg.pt",
        "SMALL":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26s-seg.pt",
        "MEDIUM":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26m-seg.pt",
        "LARGE":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26l-seg.pt",
        "XLAARGE":"https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26x-seg.pt"
    }

    
}

