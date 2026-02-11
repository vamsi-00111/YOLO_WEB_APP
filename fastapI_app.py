from yolo import YoloDetecter
from fastapi import FastAPI,UploadFile,File
import numpy as np
import cv2


yolo=YoloDetecter()



app=FastAPI()

@app.get("/")
async def home():
    return "hello! now we are detecting objects for now i only created the model for detection later on i will make sure that all tasks would be finished coding"

@app.post("/detection")
async def detect(file:UploadFile=File(...)):
    contents=await file.read()
    # Convert bytes to numpy array
    np_arr = np.frombuffer(contents, np.uint8)

    # Decode image
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    pred=yolo.detect(img)
    
    return pred
    
    
    

