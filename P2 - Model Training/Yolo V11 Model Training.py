from ultralytics import YOLO
import torch

no_devices = [i for i in range(torch.cuda.device_count())]
model = YOLO("yolo11n.pt")

results = model.train( data="dataset/dataset_train.yaml", epochs=100, batch=16, imgsz=640, device=no_devices, workers=8)

metrics = model.val()
print(f"mAP Score for Validation Data: {metrics.box.map}")

# model.export(format="onnx")