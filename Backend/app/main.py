from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from services.face_swapper import FaceSwapper
from services.face_enhancer import FaceEnhancer
from utils.image_processing import save_upload_file_tmp
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Update CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Add both localhost and 127.0.0.1
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

face_swapper = FaceSwapper()
face_enhancer = FaceEnhancer()

@app.post("/swap-face/")
async def swap_face(source: UploadFile = File(...), target: UploadFile = File(...)):
    source_path = save_upload_file_tmp(source)
    target_path = save_upload_file_tmp(target)
    
    result_path = face_swapper.swap(source_path, target_path)
    
    return FileResponse(result_path)

@app.post("/enhance-face/")
async def enhance_face(source: UploadFile = File(...)):
    image_path = save_upload_file_tmp(source)
    
    result_path = face_enhancer.enhance(image_path)
    
    return FileResponse(result_path)

@app.post("/swap-and-enhance/")
async def swap_and_enhance(source: UploadFile = File(...), target: UploadFile = File(...)):
    source_path = save_upload_file_tmp(source)
    target_path = save_upload_file_tmp(target)
    
    swapped_path = face_swapper.swap(source_path, target_path)
    result_path = face_enhancer.enhance(swapped_path)
    
    return FileResponse(result_path)

@app.get("/")
def home():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)