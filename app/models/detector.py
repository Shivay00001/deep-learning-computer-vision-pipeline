import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn, FasterRCNN_ResNet50_FPN_Weights
from app.core.config import settings

class ModelManager:
    def __init__(self):
        self.device = torch.device(settings.DEVICE)
        self.model = None
        
    def load_model(self):
        if self.model is None:
            weights = FasterRCNN_ResNet50_FPN_Weights.DEFAULT
            self.model = fasterrcnn_resnet50_fpn(weights=weights, progress=False).to(self.device)
            self.model.eval()
            self.categories = weights.meta["categories"]
            
    def predict(self, image_tensor):
        self.load_model()
        with torch.no_grad():
            predictions = self.model([image_tensor.to(self.device)])
        return predictions[0]

model_manager = ModelManager()
