# 🚀 IntelliMD: IntelliMD: A Misbehaviour Detection Framework for Cooperative Intelligent Transport Systems

Welcome to the **IntelliMD: IntelliMD: A Misbehaviour Detection Framework for Cooperative Intelligent Transport Systems** repository! This project focuses on the detection and mitigation of misbehaviours in **Cooperative Intelligent Transport Systems (C-ITS)** using a multi-layered framework. Our approach includes **Local, Cooperative, Infrastructure, and Global Intelligence** to identify and respond to malicious activities in vehicular networks.

## 🔍 About the Research

C-ITS is a transformative technology that enhances road safety and traffic efficiency through vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) communications. However, the **security and trustworthiness** of these communications are critical challenges due to potential attacks such as **false data injection, message replay, and denial-of-service (DoS) attacks**.

This project introduces **IntelliMD**, a **multi-layered detection and mitigation framework**, ensuring **adaptive, real-time response** to misbehaviours. The framework consists of the following components:
- **Local-IntelliMD**: Detects anomalies at the individual vehicle level.
- **Cooperative-IntelliMD**: Aggregates reports from nearby vehicles for collaborative misbehaviour detection.
- **Infra-IntelliMD**: Uses roadside infrastructure to validate and mitigate anomalies.
- **Global-IntelliMD**: Analyzes and mitigates large-scale misbehaviour patterns across the entire network.

## 📂 Project Structure

This repository contains Python implementations of the different IntelliMD components in subcomponents for the ease of replicating/integrating individual modules.

### 🔥 Core Components

| File | Description |
|------|------------|
| `file1.py` | **Local-IntelliMD** - Performs plausibility and consistency checks to detect anomalies at the vehicle level. |
| `file2.py` | **Cooperative-IntelliMD** - Utilizes cooperative data exchange for enhanced anomaly detection. |
| `file3.py` | **Infra-IntelliMD** - Leverages infrastructure-based validation using **RSUs** and edge computing. |
| `file4.py` | **Global-IntelliMD** - Implements large-scale misbehavior detection across multiple infrastructure nodes. |
| `feature_engineering.py` | Extracts and transforms relevant features for machine learning-based anomaly detection. |
| `real_time_detection.py` | Implements **incremental learning** for real-time misbehavior classification. |
| `performance_evaluation.py` | Evaluates the detection mechanisms using **accuracy, precision, recall, MCC, Kappa**, and **runtime metrics**. |

