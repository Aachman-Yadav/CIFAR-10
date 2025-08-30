# CIFAR-10 Image Classification with CNN 

This project implements a **Convolutional Neural Netwrok (CNN)** to classify images from the **CIFAR-10 dataset** using **Tensorflow/Keras** .
It also includes a small frontend (`app.py`) to load the trained model (`cifar10_cnn_model.keras`) and make predictions.

**Visit the deployed site-**
[Deployed Project](https://aachman-yadav-cifar-10-app-cefs8n.streamlit.app/)

---
## Project Structure
```
CIFAR-10/
├── app.py # Streamlit app for inference
├── cifar10_cnn_model.keras # Trained model file
├── requirements.txt # Python dependencies
├── venv/ # Virtual environment (ignored)
└── README.md # Project documentation
```

---

## Getting Started

**To run on your system-**

### 1. Clone the repo
```bash
git clone https://github.com/Aachman-Yadav/CIFAR-10.git
cd CIFAR-10
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
#On Linux/Mac
source venv/bin/activate
#On Windows
venv\Scripts\actiavte
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Running the App
```bash
streamlit run app.py
```
**If using plain Python Script**
```bash
python app.py
```