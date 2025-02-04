from ultralytics import YOLO
import torch

model = YOLO("runs/detect/train/weights/best.pt")
no_devices = [i for i in range(torch.cuda.device_count())]

results = model.val( data="dataset/dataset_train.yaml", split="test", batch=16, imgsz=640, conf=0.5, iou=0.6, device=no_devices, workers=8)

print(f"mAP50: {results.box.map50}")
print(f"mAP50-95: {results.box.map}")
print(f"F1 Score: {results.box.f1}")