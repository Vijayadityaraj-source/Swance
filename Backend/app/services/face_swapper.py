import cv2
import insightface
from utils.image_processing import load_image, save_image

class FaceSwapper:
    def __init__(self):
        self.model = insightface.app.FaceAnalysis()
        self.model.prepare(ctx_id=0, det_size=(640, 640))
        self.swapper = insightface.model_zoo.get_model('data\models\inswapper_128.onnx')

    def swap(self, source_path: str, target_path: str) -> str:
        source_img = load_image(source_path)
        target_img = load_image(target_path)

        source_face = self.model.get(source_img)[0]
        target_faces = self.model.get(target_img)

        for face in target_faces:
            target_img = self.swapper.get(target_img, face, source_face, paste_back=True)

        result_path = 'output_swapped.jpg'
        save_image(result_path, target_img)
        return result_path