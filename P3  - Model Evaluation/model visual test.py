import cv2
from ultralytics import YOLO

model_path = r""
video_path = r""

model = YOLO(model_path)
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    height, width = frame.shape[:2]
    frame = cv2.resize(frame, (width // 2, height // 2))
    if not ret:
        break

    results = model.predict(source=frame, save=False, conf=0.25)

    img_with_boxes = results[0].plot()

    cv2.imshow("YOLO Detection", img_with_boxes)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
