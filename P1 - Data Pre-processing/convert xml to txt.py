import os
import xml.etree.ElementTree as ET

IMAGES_FOLDER = "Kaggle Dataseet/images"
ANNOTATIONS_FOLDER = "Kaggle Dataseet/annotations"
OUTPUT_FOLDER = "Kaggle Dataseet/yolo_annotations"

###### Here correctley mention the class name and class id from xml file
CLASS_MAPPING = {
    "head": 0,
    "helmet": 1,
}

def create_output_folder(output_folder):
    """Create the output folder if it doesn't exist."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

def parse_xml_annotation(xml_file):
    """Parse an XML file and return the root element."""
    tree = ET.parse(xml_file)
    return tree.getroot()

def convert_bounding_box(size, bndbox):
    """
    Convert bounding box coordinates from XML format to YOLO format.
    YOLO format: [class_id, x_center, y_center, width, height] (normalized).
    """
    width, height = size
    xmin = int(bndbox.find("xmin").text)
    ymin = int(bndbox.find("ymin").text)
    xmax = int(bndbox.find("xmax").text)
    ymax = int(bndbox.find("ymax").text)

    x_center = (xmin + xmax) / 2 / width
    y_center = (ymin + ymax) / 2 / height
    box_width = (xmax - xmin) / width
    box_height = (ymax - ymin) / height

    return x_center, y_center, box_width, box_height

def process_annotation(root):
    """
    Process an XML annotation and return YOLO-formatted annotations.
    Skips the 'person' class entirely.
    """
    size = root.find("size")
    width = int(size.find("width").text)
    height = int(size.find("height").text)
    size = (width, height)

    yolo_annotations = []
    for obj in root.findall("object"):
        class_name = obj.find("name").text.lower()
        if class_name not in CLASS_MAPPING:
            continue

        class_id = CLASS_MAPPING[class_name]
        bndbox = obj.find("bndbox")
        x_center, y_center, box_width, box_height = convert_bounding_box(size, bndbox)

        yolo_annotations.append(f"{class_id} {x_center} {y_center} {box_width} {box_height}")

    return yolo_annotations

def save_yolo_annotation(yolo_annotations, output_file):
    """Save YOLO annotations to a file."""
    with open(output_file, "w") as f:
        f.write("\n".join(yolo_annotations))

def convert_annotation_to_yolo(xml_file, output_folder):
    """Convert a single XML annotation to YOLO format and save it."""
    root = parse_xml_annotation(xml_file)
    yolo_annotations = process_annotation(root)

    output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(xml_file))[0] + ".txt")
    save_yolo_annotation(yolo_annotations, output_file)

def main():
    """Main function to convert all XML annotations to YOLO format."""
    create_output_folder(OUTPUT_FOLDER)

    for xml_file in os.listdir(ANNOTATIONS_FOLDER):
        if xml_file.endswith(".xml"):
            xml_path = os.path.join(ANNOTATIONS_FOLDER, xml_file)
            convert_annotation_to_yolo(xml_path, OUTPUT_FOLDER)

    print(f"YOLO annotations saved in '{OUTPUT_FOLDER}'.")

if __name__ == "__main__":
    main()



##############################################################################################################################################################################################################################################################################################################################################################################




# import os
# import xml.etree.ElementTree as ET

# IMAGES_FOLDER = "Kaggle Dataseet/images"
# ANNOTATIONS_FOLDER = "Kaggle Dataseet/annotations"
# OUTPUT_FOLDER = "Kaggle Dataseet/yolo_annotations"

# CLASS_MAPPING = {
#     "head": 0,  # No-helmet
#     "helmet": 1,  # Helmet
#     "person": 2,  # Human
# }

# def create_output_folder(output_folder):
#     """Create the output folder if it doesn't exist."""
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

# def parse_xml_annotation(xml_file):
#     """Parse an XML file and return the root element."""
#     tree = ET.parse(xml_file)
#     return tree.getroot()

# def convert_bounding_box(size, bndbox):
#     """
#     Convert bounding box coordinates from XML format to YOLO format.
#     YOLO format: [class_id, x_center, y_center, width, height] (normalized).
#     """
#     width, height = size
#     xmin = int(bndbox.find("xmin").text)
#     ymin = int(bndbox.find("ymin").text)
#     xmax = int(bndbox.find("xmax").text)
#     ymax = int(bndbox.find("ymax").text)

#     x_center = (xmin + xmax) / 2 / width
#     y_center = (ymin + ymax) / 2 / height
#     box_width = (xmax - xmin) / width
#     box_height = (ymax - ymin) / height

#     return x_center, y_center, box_width, box_height

# def process_annotation(root):
#     """
#     Process an XML annotation and return YOLO-formatted annotations.
#     """
#     size = root.find("size")
#     width = int(size.find("width").text)
#     height = int(size.find("height").text)
#     size = (width, height)

#     yolo_annotations = []
#     for obj in root.findall("object"):
#         class_name = obj.find("name").text.lower()
#         if class_name not in CLASS_MAPPING:
#             print(f"Warning: Unknown class '{class_name}' found in annotation. Skipping.")
#             continue

#         class_id = CLASS_MAPPING[class_name]
#         bndbox = obj.find("bndbox")
#         x_center, y_center, box_width, box_height = convert_bounding_box(size, bndbox)

#         yolo_annotations.append(f"{class_id} {x_center} {y_center} {box_width} {box_height}")

#     return yolo_annotations

# def save_yolo_annotation(yolo_annotations, output_file):
#     """Save YOLO annotations to a file."""
#     with open(output_file, "w") as f:
#         f.write("\n".join(yolo_annotations))

# def convert_annotation_to_yolo(xml_file, output_folder):
#     """Convert a single XML annotation to YOLO format and save it."""
#     root = parse_xml_annotation(xml_file)
#     yolo_annotations = process_annotation(root)

#     output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(xml_file))[0] + ".txt")
#     save_yolo_annotation(yolo_annotations, output_file)

# def main():
#     """Main function to convert all XML annotations to YOLO format."""
#     create_output_folder(OUTPUT_FOLDER)

#     for xml_file in os.listdir(ANNOTATIONS_FOLDER):
#         if xml_file.endswith(".xml"):
#             xml_path = os.path.join(ANNOTATIONS_FOLDER, xml_file)
#             convert_annotation_to_yolo(xml_path, OUTPUT_FOLDER)

#     print(f"YOLO annotations saved in '{OUTPUT_FOLDER}'.")

# if __name__ == "__main__":
#     main()