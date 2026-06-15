# 🎓 Smart Exam Proctoring System

<div align="center">

### AI-Powered Real-Time Examination Monitoring Platform

Detects suspicious activities during online examinations using **Computer Vision**, **Deep Learning**, and **Real-Time Analytics**.

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge\&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-green?style=for-the-badge\&logo=opencv)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object_Detection-red?style=for-the-badge)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Face_Tracking-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-ff4b4b?style=for-the-badge\&logo=streamlit)

</div>

---

## 📌 Project Overview

The Smart Exam Proctoring System is an AI-driven online examination monitoring solution designed to enhance academic integrity by detecting suspicious activities in real time.

The system continuously analyzes webcam feeds and automatically identifies potential examination violations such as:

* Multiple people appearing in the frame
* Mobile phone usage
* Candidate absence
* Face visibility issues
* Suspicious movements
* Unauthorized object detection

Whenever a violation occurs, the system captures evidence, records logs, and displays events through a real-time dashboard.

---

## 🚀 Key Features

### 👤 Face Monitoring

* Real-time face detection
* Candidate presence verification
* Multiple face detection
* Face count monitoring

### 📱 Mobile Phone Detection

* YOLOv8-based object detection
* Detects mobile phones during exams
* Generates instant warnings

### 📸 Evidence Collection

* Automatic screenshot capture
* Timestamp-based evidence storage
* Violation image archiving

### 📊 Dashboard Monitoring

* Streamlit-powered dashboard
* Live violation records
* Screenshot gallery
* Statistics and analytics

### 📝 Violation Logging

* CSV-based event logging
* Timestamp tracking
* Violation history management

---

## 🧠 System Workflow

```text
Webcam Feed
      │
      ▼
Face Detection
      │
      ▼
Object Detection (YOLOv8)
      │
      ▼
Violation Analysis
      │
      ▼
Screenshot Capture
      │
      ▼
CSV Logging
      │
      ▼
Dashboard Visualization
```

---

## 🏗️ Project Architecture

```text
Smart Exam Proctoring System
│
├── dashboard.py
├── face_detection.py
├── phone_detection.py
├── logger.py
│
├── logs
│   └── violations.csv
│
├── screenshots
│
├── models
│
└── README.md
```

---

## 🛠️ Technology Stack

| Technology | Purpose              |
| ---------- | -------------------- |
| Python     | Core Development     |
| OpenCV     | Image Processing     |
| MediaPipe  | Face Detection       |
| YOLOv8     | Object Detection     |
| Streamlit  | Dashboard Interface  |
| Pandas     | Data Management      |
| NumPy      | Numerical Processing |

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https:https://github.com/vijaydevverse/Smart-Exam-Proctoring-System

cd Smart-Exam-Proctoring-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Face Detection

```bash
python face_detection.py
```

### Phone Detection

```bash
python phone_detection.py
```

### Dashboard

```bash
streamlit run dashboard.py
```

---

## 📊 Violation Examples

| Violation            | Detection |
| -------------------- | --------- |
| Multiple Faces       | ✅         |
| Mobile Phone Usage   | ✅         |
| Candidate Missing    | Planned   |
| Looking Away         | Planned   |
| Head Down            | Planned   |
| Unauthorized Objects | Planned   |

---

## 📸 Screenshots

Add your project screenshots here after uploading:

```text
assets/
├── dashboard.png
├── face_detection.png
├── phone_detection.png
├── violations.png
```

Example:

```markdown
![Dashboard](assets/dashboard.png)
```

---

## 🔒 Future Enhancements

* Head Pose Estimation
* Eye Gaze Tracking
* Candidate Absence Detection
* Email Alert System
* Telegram Notifications
* Admin Control Panel
* Cloud Database Integration
* Real-Time Report Generation
* Custom YOLO Training for Cheat Materials
* Multi-Camera Monitoring

---

## 🎯 Learning Outcomes

This project demonstrates practical implementation of:

* Computer Vision
* Deep Learning
* Real-Time Monitoring Systems
* Object Detection
* Human Activity Analysis
* AI-Based Security Applications
* Dashboard Development

---

## 📈 Resume Description

> Developed an AI-powered Smart Exam Proctoring System using OpenCV, MediaPipe, YOLOv8, and Streamlit. The platform performs real-time face monitoring, mobile phone detection, evidence capture, violation logging, and dashboard-based analytics to enhance online examination integrity.

---

## 👨‍💻 Author

**Vijay Krishnan P.M.**

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share with others

---

<div align="center">

### 🚀 Building Smarter and Safer Online Examinations with AI

</div>
