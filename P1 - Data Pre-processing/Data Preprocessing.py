import os
import cv2
import albumentations as A
from multiprocessing import Pool

def preprocess_and_augment(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    transform = A.Compose([
        A.HorizontalFlip(p=0.5),
        A.RandomBrightnessContrast(p=0.5),
        A.GaussianBlur(p=0.3),
        A.ToGray(p=0.2),
        A.Affine(shear=(-10, 10), p=0.5),
        A.Resize(640, 640),
    ])
    
    files = os.listdir(input_folder)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp'))]
    
    def process_image(image_file):
        try:
            img_path = os.path.join(input_folder, image_file)
            img = cv2.imread(img_path)
            if img is None:
                print(f"Error reading image: {img_path}")
                return

            output_original_path = os.path.join(output_folder, image_file)
            cv2.imwrite(output_original_path, img)
            print(f"Saved original: {output_original_path}")

            augmented = transform(image=img)
            augmented_img = augmented['image']

            augmented_filename = f"{os.path.splitext(image_file)[0]}_aug{os.path.splitext(image_file)[1]}"
            output_augmented_path = os.path.join(output_folder, augmented_filename)
            cv2.imwrite(output_augmented_path, augmented_img)
            print(f"Saved augmented: {output_augmented_path}")
        except Exception as e:
            print(f"Error processing {image_file}: {e}")
    
    with Pool(processes=os.cpu_count()) as pool:
        pool.map(process_image, image_files)

input_folder = 'P1 - Data Pre-processing\images'
output_folder = 'P1 - Data Pre-processing\Annotated Images'
preprocess_and_augment(input_folder, output_folder)