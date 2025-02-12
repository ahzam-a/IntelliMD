🚀 Misbehavior Detection & Mitigation in C-ITS

Welcome to the Misbehavior Detection & Mitigation repository! This project focuses on the detection and mitigation of misbehaviors in Cooperative Intelligent Transport Systems (C-ITS) using a multi-layered framework. Our approach includes Local, Cooperative, Infrastructure, and Global Intelligence to identify and respond to malicious activities in vehicular networks.

🔍 About the Research

C-ITS is a transformative technology that enhances road safety and traffic efficiency through vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) communications. However, the security and trustworthiness of these communications are critical challenges due to potential attacks such as false data injection, Sybil attacks, message replay, and denial-of-service (DoS) attacks.

This project introduces IntelliMD, a multi-layered detection and mitigation framework, ensuring adaptive, real-time response to misbehaviors. The framework consists of the following components:

Local-IntelliMD: Detects anomalies at the individual vehicle level.

Cooperative-IntelliMD: Aggregates reports from nearby vehicles for collaborative misbehavior detection.

Infra-IntelliMD: Uses roadside infrastructure to validate and mitigate anomalies.

Global-IntelliMD: Analyzes large-scale misbehavior patterns across the entire network.

📂 Project Structure

This repository contains Python implementations of the different IntelliMD components, along with utility scripts for real-time classification, feature engineering, and performance evaluation.

🔥 Core Components

File

Description

file1.py

Local-IntelliMD - Performs plausibility and consistency checks to detect anomalies at the vehicle level.

file2.py

Cooperative-IntelliMD - Utilizes cooperative data exchange for enhanced anomaly detection.

file3.py

Infra-IntelliMD - Leverages infrastructure-based validation using RSUs and edge computing.

file4.py

Global-IntelliMD - Implements large-scale misbehavior detection across multiple infrastructure nodes.

feature_engineering.py

Extracts and transforms relevant features for machine learning-based anomaly detection.

real_time_detection.py

Implements incremental learning for real-time misbehavior classification.

performance_evaluation.py

Evaluates the detection mechanisms using accuracy, precision, recall, MCC, Kappa, and runtime metrics.

🚀 Getting Started

Clone the repository:

git clone https://github.com/your-repo/misbehavior-detection.git
cd misbehavior-detection

Install dependencies:

pip install -r requirements.txt

Run a specific detection module:

python file1.py  # Runs Local-IntelliMD

📊 Performance Metrics

Each detection method is evaluated using:

Detection Accuracy ✅

False Positive Rate (FPR) & False Negative Rate (FNR) 🚨

Detection Time (ms) ⏳

Memory & CPU Usage 💾

Confidence Intervals for Stability Analysis 📈

📌 Key Features

✔ Real-time Detection & Mitigation✔ Multi-layered Decision-Making✔ Machine Learning Integration (Random Forest, ADWIN, LSTM)✔ Scalable & Adaptive Thresholds✔ Comprehensive Evaluation & Metrics Tracking

📢 Contributing

We welcome contributions from the research and cybersecurity communities! Feel free to submit pull requests, report issues, or share improvements. 🚀

📜 License

This project is licensed under the MIT License - feel free to modify and use it for research and development purposes.

🚗 Securing the Roads of the Future with IntelliMD! 🚦
