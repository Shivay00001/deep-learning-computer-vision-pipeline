from fastapi import APIRouter, UploadFile, File, HTTPException
from app.models.detector import model_manager
from app.core.config import settings
from PIL import Image
import torch
from torchvision import transforms
import io

router = APIRouter()

# Simple transformation to tensor
transform = transforms.Compose([
    transforms.ToTensor(),
])

@router.post("/detect")
async def detect_objects(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
        
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        image_tensor = transform(image)
        
        prediction = model_manager.predict(image_tensor)
        
        # Filter by confidence
        scores = prediction['scores'].tolist()
        labels = prediction['labels'].tolist()
        boxes = prediction['boxes'].tolist()
        
        results = []
        for score, label, box in zip(scores, labels, boxes):
            if score >= settings.SCORE_THRESHOLD:
                results.append({
                    "label": model_manager.categories[label],
                    "score": score,
                    "box": box
                })
                
        return {"filename": file.filename, "detections": results}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/models")
async def list_models():
    return {"available_models": [settings.DEFAULT_MODEL]}
