import cv2
import gfpgan
from utils.image_processing import load_image, save_image

class FaceEnhancer:
    def __init__(self):
        self.model = gfpgan.GFPGANer(model_path='data\models\GFPGANv1.4.pth', upscale=2)

    def enhance(self, image_path: str) -> str:
        img = load_image(image_path)
        
        _, _, output = self.model.enhance(img, has_aligned=False, only_center_face=False, paste_back=True)
        
        result_path = 'output_enhanced.jpg'
        save_image(result_path, output)
        return result_path