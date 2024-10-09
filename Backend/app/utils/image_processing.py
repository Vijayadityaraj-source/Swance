import cv2
import numpy as np
from fastapi import UploadFile
import shutil
import os
from tempfile import NamedTemporaryFile

def load_image(path: str) -> np.ndarray:
    return cv2.imread(path)

def save_image(path: str, image: np.ndarray) -> None:
    cv2.imwrite(path, image)

def save_upload_file_tmp(upload_file: UploadFile) -> str:
    try:
        suffix = os.path.splitext(upload_file.filename)[1]
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = tmp.name
    finally:
        upload_file.file.close()
    return tmp_path