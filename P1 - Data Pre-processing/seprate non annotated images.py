import os
import shutil

def move_images_without_annotations(image_folder, annotation_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get list of files in both folders
    image_files = set(os.listdir(image_folder))
    annotation_files = set(os.listdir(annotation_folder))

    # Iterate through image files
    for image_file in image_files:
        # Get the base name without extension
        image_name = os.path.splitext(image_file)[0]

        # Check if there is a corresponding annotation file
        annotation_found = False
        for annotation_file in annotation_files:
            annotation_name = os.path.splitext(annotation_file)[0]
            if annotation_name == image_name:
                annotation_found = True
                break

        # If no annotation found, move the image to the output folder
        if not annotation_found:
            image_path = os.path.join(image_folder, image_file)
            output_path = os.path.join(output_folder, image_file)
            shutil.move(image_path, output_path)
            print(f"Moved {image_file} to {output_folder}")

if __name__ == "__main__":
    # Define the paths to the folders
    image_folder = "P1 - Data Pre-processing/Jayesh"
    annotation_folder = "P1 - Data Pre-processing/Jayesh_annotations"
    output_folder = "media/non_annotated"

    # Call the function to move images without annotations
    move_images_without_annotations(image_folder, annotation_folder, output_folder)