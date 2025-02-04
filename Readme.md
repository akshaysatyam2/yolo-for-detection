# **PPE Detection Project**

This project aims to detect **Personal Protective Equipment (PPE)** using **YOLOv11** or other YOLO models of your choice. It includes **data preprocessing, model training, and evaluation** to ensure accurate detection of PPE in images.

---

## **Project Structure**

```
Main Directory
│   .env
│   .gitignore
│   requirements.txt
│   README.md
│
├── dataset
│   ├── dataset_train.yaml
│   ├── images
│   │   ├── test
│   │   ├── train
│   │   └── val
│   └── labels
│       ├── test
│       ├── train
│       └── val
│
├── P1 - Data Preprocessing
│   ├── data_preprocessing.py  # Main script to preprocess images and labels
│   ├── convert_xml_to_txt.py  # Converts annotation files from XML (Pascal VOC) to TXT (YOLO format)
│   ├── display_labels.py      # Displays dataset labels and their distributions
│   └── separate_non_annotated_images.py  # Filters out images without annotations
│
├── P2 - Model Training
│   ├── yolo_v11_model_training.py  # Script for training YOLOv11 model
│   ├── model_loader.py  # Loads and initializes the YOLO model
│   └── augment_data.py  # Applies data augmentation techniques to improve model performance
│
└── P3 - Model Evaluation
    ├── model_evaluation.py  # Evaluates the trained YOLO model using test data
    ├── model_visual_test.py  # Visualizes model predictions on sample images
    └── performance_metrics.py  # Computes key performance metrics (mAP, precision, recall)
```

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/akshaysatyam2/yolo-for-detection.git
cd yolo-for-detection
```

### **2. Create and Activate a Virtual Environment**
```bash
python -m venv venv
```
- **Windows:**  
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**  
  ```bash
  source venv/bin/activate
  ```

### **3. Install Required Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**
- Rename `.env.example` to `.env` and configure necessary variables.

---

## **Usage Guide**

### **1. Data Preprocessing**
Preprocess the dataset before training.

**Run:**
```bash
python "P1 - Data Preprocessing/data_preprocessing.py"
```

### **2. Model Training**
Train the YOLOv11 model on the dataset.

**Run:**
```bash
python "P2 - Model Training/yolo_v11_model_training.py"
```

### **3. Model Evaluation**
Evaluate the trained model’s performance.

**Run:**
```bash
python "P3 - Model Evaluation/model_evaluation.py"
```

---

## **Dataset Structure**
The dataset follows this format:

```
dataset/
├── images/
│   ├── test/
│   ├── train/
│   └── val/
└── labels/
    ├── test/
    ├── train/
    └── val/
```
- **Images:** Store images in `images/train`, `images/val`, and `images/test`.
- **Labels:** Store corresponding labels in `labels/train`, `labels/val`, and `labels/test`.

---

## **Configuration Files**

### **Yaml Configuration (`dataset_train.yaml`)**
```yaml
train: dataset/images/train
val: dataset/images/val
test: dataset/images/test
nc: 2
names: ["Helmet", "No Helmet"]
epochs: 50
batch_size: 16
image_size: 640
```

---

## **Required Dependencies**
This project requires:

- `ultralytics`
- `opencv-python`
- `numpy`
- `matplotlib`
- `pandas`
- `python-dotenv`

Install with:
```bash
pip install -r requirements.txt
```

---

## **Deactivating the Virtual Environment**
When done, deactivate the virtual environment:
```bash
deactivate
```

---

## **Contact Information**
For questions or contributions:
- **Name:** Akshay Kumar  
- **Email:** [akshaysatyam2003@gmail.com](mailto:akshaysatyam2003@gmail.com)  
- **GitHub:** [@akshaysatyam2](https://github.com/akshaysatyam2)

---

