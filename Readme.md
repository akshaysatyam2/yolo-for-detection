# PPE Detection Project

This project is designed to detect Personal Protective Equipment (PPE) using YOLOv11. It includes data preprocessing, model training, and evaluation steps.

---

## **Project Structure**

```
Main Directory:.
│   .env
│   .gitignore
│   requirements.txt
│
├───dataset
│   ├───dataset.yaml
│   ├───images
│   │   ├───test
│   │   ├───train
│   │   └───val
│   └───labels
│       ├───test
│       ├───train
│       └───val
├───P1 - Data Pre-processing
│       Data Preprocessing.py
│       
├───P2 - Model Training
│       Yolo V11 Model Training.py
│
└───P3 - Model Evaluation
        Model Evaluation.py
```

---

## **Setup**

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a Python Virtual Environment:**
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

3. **Install Dependencies:**
   Install the required Python packages using:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   - Rename `.env.example` to `.env` and update the environment variables as needed.

---

## **Usage**

### **1. Data Preprocessing**

The `P1 - Data Pre-processing` folder contains the script for preprocessing the dataset.

- **Script:** `Data Preprocessing.py`
- **Input:** Raw images and labels in the `P1 - Data Pre-processing\images` folder.
- **Output:** Preprocessed images and labels in the `P1 - Data Pre-processing\Annotated Images` folders.

**Run the Script:**
```bash
python "P1 - Data Pre-processing/Data Preprocessing.py"
```

---

### **2. Model Training**

The `P2 - Model Training` folder contains the script for training the YOLOv11 model.

- **Script:** `Yolo V11 Model Training.py`
- **Configuration:** `dataset.yaml`
- **Input:** Preprocessed images and labels from the `dataset` folder.
- **Output:** Trained model weights (e.g., `yolov11n.pt`).

**Run the Script:**
```bash
python "P2 - Model Training/Yolo V11 Model Training.py"
```

---

### **3. Model Evaluation**

The `P3 - Model Evaluation` folder contains the script for evaluating the trained model.

- **Script:** `Model Evaluation.py`
- **Configuration:** `dataset.yaml`
- **Input:** Trained model weights (e.g., `yolov11n.pt`) and test dataset.
- **Output:** Evaluation metrics (e.g., mAP, precision, recall).

**Run the Script:**
```bash
python "P3 - Model Evaluation/Model Evaluation.py"
```

---

## **Dataset**

The dataset is organized in the following structure:

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

- **Images:** Store your images in the `images` subfolders (`train`, `val`, `test`).
- **Labels:** Store your corresponding labels in the `labels` subfolders (`train`, `val`, `test`).

---

## **Configuration**

### **Training Configuration (`P2 - Model Training/dataset.yaml`):**
```yaml
train: dataset/images/train
val: dataset/images/val
nc: 2
names: ["class1", "class2"]
```

### **Evaluation Configuration (`P3 - Model Evaluation/dataset.yaml`):**
```yaml
test: dataset/images/test
nc: 2
names: ["class1", "class2"]
```

---

## **Dependencies**

The project requires the following Python packages:

- `ultralytics` (for YOLOv11)
- `opencv-python`
- `numpy`
- `python-dotenv`

Install them using:
```bash
pip install -r requirements.txt
```

---

## **Deactivating the Virtual Environment**

When you're done working on the project, deactivate the virtual environment by running:
```bash
deactivate
```

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**

For questions or support, contact:
- **Name:** Akshay Kumar
- **Email:** [Your Email](mailto:akshaysatyam2003@gmail.com)
- **GitHub:** [Your GitHub Profile](https://github.com/akshaysatyam2)
