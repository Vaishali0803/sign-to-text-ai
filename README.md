# Sign2Text AI

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)
![Scikit-Learn](https://img.shields.io/badge/Model-Random%20Forest-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

</p>

<h3 align="center">
Real-Time Sign Language to Text using Computer Vision and Machine Learning
</h3>

<p align="center">
An AI-powered application that recognizes sign language gestures from a live webcam feed and converts them into readable text captions in real time.
</p>

---

# Table of Contents

- Overview
- Problem Statement
- Our Solution
- Features
- System Workflow
- AI Pipeline
- Dataset and Model Training
- Technologies Used
- Project Structure
- Installation
- Usage
- Results
- Future Enhancements
- Team
- License

---

# Overview

Communication between people who use sign language and those who do not remains a major challenge. Most existing sign language recognition systems recognize only individual alphabets, requiring users to spell every word letter by letter, which makes conversations slow and unnatural.

**Sign2Text AI** is a real-time sign language recognition system that uses Computer Vision and Machine Learning to recognize complete sign gestures and convert them into text instantly.

The application captures live video through a webcam, extracts hand and upper-body landmarks using MediaPipe, generates numerical features, and predicts the performed sign using a Machine Learning model trained on a **custom dataset created by our team**.

The project is lightweight, runs entirely on a CPU, and can easily be extended to support larger vocabularies and continuous sentence recognition.

---

# Problem Statement

Millions of people worldwide rely on sign language as their primary mode of communication. However, communication between sign language users and the general public remains difficult because most people do not understand sign language.

Existing recognition systems have several limitations:

- They recognize only alphabets instead of complete words.
- Users must spell every word manually.
- Many systems rely on publicly available datasets.
- Most applications are not suitable for natural real-time conversations.

There is a need for an intelligent system that can recognize complete sign gestures quickly and accurately to make communication more seamless.

---

# Our Solution

Sign2Text AI addresses these challenges by recognizing complete sign gestures using a custom-trained Machine Learning model.

Our system performs the following steps:

- Captures live video from a webcam.
- Detects hand and body landmarks using MediaPipe.
- Extracts numerical landmark features.
- Predicts the corresponding sign using a Random Forest classifier.
- Displays the recognized word instantly on the screen.
- Builds sentences by combining consecutive predictions.

Unlike many existing projects, we **created our own dataset**, manually labeled every sample, trained our own Machine Learning model, and integrated it into a real-time application.

---

<img width="920" height="720" alt="Screenshot 2026-07-31 221310" src="https://github.com/user-attachments/assets/9a0996d2-37a2-4a1e-bb07-2c8e3394dfb5" />

<img width="1036" height="843" alt="Screenshot 2026-07-31 221332" src="https://github.com/user-attachments/assets/f2c6a975-e65a-49eb-99be-b921d6834ed4" />



# Features

- Real-time webcam-based sign recognition
- Hand and pose landmark detection using MediaPipe
- Custom dataset creation pipeline
- Machine Learning-based word prediction
- Live caption generation
- Lightweight CPU inference
- Easy to extend with new gestures
- Cross-platform support
- Modular project structure

---

# System Workflow

```text
                Webcam
                   │
                   ▼
        OpenCV Video Capture
                   │
                   ▼
     MediaPipe Landmark Detection
                   │
                   ▼
      Feature Extraction (144 Features)
                   │
                   ▼
      Random Forest Classifier
                   │
                   ▼
        Predicted Sign
                   │
                   ▼
      Live Text Caption Display
```

---

# AI Pipeline

### Step 1 – Video Capture

The webcam continuously captures live video frames using OpenCV.

### Step 2 – Landmark Detection

MediaPipe detects important body landmarks including:

- Left Hand
- Right Hand
- Shoulders
- Elbows
- Wrists

### Step 3 – Feature Extraction

The detected landmarks are converted into numerical feature vectors.

| Feature Type | Count |
|--------------|------:|
| Pose Features | 18 |
| Hand Features | 126 |
| **Total Features** | **144** |

### Step 4 – Machine Learning Prediction

The trained Random Forest classifier predicts the performed sign from the extracted features.

### Step 5 – Live Caption Generation

The predicted word is displayed instantly on the screen.

Example:

```
HELLO

↓

PLEASE

↓

HELP
```

These predictions can be combined to form meaningful sentences.

---

# Dataset and Model Training

One of the major contributions of this project is the creation of a **custom sign language dataset**.

Instead of relying on existing datasets, we collected our own training data by recording sign language gestures through a webcam. MediaPipe was used to extract hand and body landmarks from each recording, and every sample was manually labeled before training.

The extracted landmark coordinates were converted into numerical feature vectors and used to train a **Random Forest classifier**, enabling accurate real-time sign recognition.

## Dataset Creation Workflow

```text
Sign Gesture Recording
          │
          ▼
MediaPipe Landmark Detection
          │
          ▼
Feature Extraction
          │
          ▼
Manual Data Labeling
          │
          ▼
CSV Dataset Generation
          │
          ▼
Random Forest Model Training
          │
          ▼
Real-Time Prediction
```

## Dataset Statistics

| Property | Value |
|----------|------:|
| Dataset Type | Custom |
| Number of Classes | 10 |
| Samples per Class | 200 |
| Total Samples | 2000 |
| Features per Sample | 144 |
| Machine Learning Model | Random Forest |

### Supported Words

- HELLO
- HELP
- YES
- NO
- PLEASE
- HAPPY
- GOOD MORNING
- I
- I AM
- I LOVE YOU

---

# Technologies Used

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Computer Vision | OpenCV |
| Landmark Detection | MediaPipe |
| Machine Learning | Scikit-learn |
| Model | Random Forest Classifier |
| Data Processing | NumPy, Pandas |

---

# Project Structure

```text
Sign2Text-AI/
│
├── dataset/
│ ├── raw/
│ ├── processed/
│ └── dataset.csv
│
├── model/
│ └── random_forest_model.pkl
│
├── scripts/
│ ├── collect_data.py
│ ├── preprocess.py
│ ├── train_model.py
│ └── predict.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Sign2Text-AI.git
```

Navigate to the project directory:

```bash
cd Sign2Text-AI
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

Start the real-time recognition system:

```bash
python predict.py
```

The webcam will open automatically. Perform one of the supported sign gestures in front of the camera, and the predicted word will be displayed on the screen in real time.

---

# Results

The system successfully:

- Detects hand and upper-body landmarks in real time.
- Extracts 144 numerical features from each frame.
- Predicts supported sign gestures using a Random Forest classifier.
- Displays recognized words as live captions.
- Runs efficiently on standard CPU hardware without requiring a dedicated GPU.

---

# Future Enhancements

- Continuous sentence recognition
- Text-to-Speech conversion
- Speech-to-Sign translation
- Support for larger sign vocabularies
- Deep Learning models (LSTM/Transformer)
- Mobile application deployment
- Cloud-based inference
- Multi-language support

---

# Team

Developed as a hackathon project by our team using Computer Vision, Machine Learning, and Artificial Intelligence.

---

# License

This project is licensed under the MIT License.
