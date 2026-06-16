from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from yolo import YoloDetecter
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
import io





app=FastAPI()
app.title="Welcome to my cv project its still basic though"
app.version="1.1.0"

@app.get("/",tags=["Home"])
def home():
    return HTMLResponse ("<h1> this is home page </h>")






@app.post("/detect",tags=["detect image "])
async def detect_api(model_size: str="MEDIUM",device: str |None=None,file: UploadFile = File(...)):
    contents = await file.read()
    yolo=YoloDetecter(size=model_size,device=device)

    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    result_img = yolo.detect(img)  

    _, buffer = cv2.imencode(".jpg", result_img)

    return StreamingResponse(
        io.BytesIO(buffer.tobytes()),
        media_type="image/jpeg"
    )
    
    
@app.post("/segment",tags=["segment image"])
async def detect_api(model_size: str="MEDIUM",device: str |None=None,file: UploadFile = File(...)):
    contents = await file.read()
    yolo=YoloDetecter(task="SEGMENTATION",size=model_size,device=device)

    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    result_img = yolo.segment_image(img)  

    _, buffer = cv2.imencode(".jpg", result_img)

    return StreamingResponse(
        io.BytesIO(buffer.tobytes()),
        media_type="image/jpeg"
    )