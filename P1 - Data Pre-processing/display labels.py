import os
import cv2

import shutil

def display_images_with_labels(image_folder, label_folder, move_image_folder, move_label_folder):
    os.makedirs(move_image_folder, exist_ok=True)
    os.makedirs(move_label_folder, exist_ok=True)

    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]
    if not image_files:
        print(f"No images found in {image_folder}.")
        return

    print(f"Found {len(image_files)} images.")
    image_files.sort()

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = cv2.imread(image_path)
        if image is None:
            print(f"Failed to load image: {image_file}")
            continue

        height, width = image.shape[:2]
        resized_image = cv2.resize(image, (width // 2, height // 2))

        label_file = os.path.splitext(image_file)[0] + '.txt'
        label_path = os.path.join(label_folder, label_file)

        if os.path.exists(label_path):
            with open(label_path, 'r') as f:
                labels = f.readlines()

            for label in labels:
                try:
                    class_id, x_center, y_center, box_width, box_height = map(float, label.strip().split())
                    h, w = resized_image.shape[:2]
                    x1 = int((x_center - box_width / 2) * w)
                    y1 = int((y_center - box_height / 2) * h)
                    x2 = int((x_center + box_width / 2) * w)
                    y2 = int((y_center + box_height / 2) * h)
                    cv2.rectangle(resized_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(resized_image, f'Class {int(class_id)}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                except ValueError:
                    print(f"Invalid label format in {label_file}.")
        else:
            print(f"No label file found for {image_file}.")

        cv2.imshow('Image with Labels (Half Resolution)', resized_image)
        key = cv2.waitKey(0) & 0xFF

        if key == ord('d'):
            shutil.move(image_path, os.path.join(move_image_folder, image_file))
            if os.path.exists(label_path):
                shutil.move(label_path, os.path.join(move_label_folder, label_file))
            print(f"Moved {image_file} and {label_file} to deletion folders.")
        elif key == ord('o'):
            print(f"Kept {image_file} and {label_file}.")
        elif key == 27:
            break

    cv2.destroyAllWindows()


image_folder = r''
label_folder = r''
move_image_folder = r''
move_label_folder = r''

display_images_with_labels(image_folder, label_folder, move_image_folder, move_label_folder)