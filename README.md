# 🚀 IntelliMD: A Misbehaviour Detection Framework for Cooperative Intelligent Transport Systems

Welcome to the **IntelliMD: A Misbehaviour Detection Framework for Cooperative Intelligent Transport Systems** repository! This project focuses on the detection and mitigation of misbehaviours in **Cooperative Intelligent Transport Systems (C-ITS)** using a multi-layered framework. Our approach includes **Local, Cooperative, Infrastructure, and Global Intelligence** to identify and respond to malicious activities in vehicular networks.

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
| `file4.py` | **Global-IntelliMD** - Implements large-scale misbehaviour detection across multiple infrastructure nodes. |
| `feature_engineering.py` | Extracts and transforms relevant features for machine learning-based anomaly detection. |
| `real_time_detection.py` | Implements **incremental learning** for real-time misbehavior classification. |
| `performance_evaluation.py` | Evaluates the detection mechanisms using **accuracy, precision, recall, MCC, Kappa**, and **runtime metrics**. |


---

## 📜 Publications and Citations  

This research has led to **multiple publications** in peer-reviewed **journals and conferences** related to **C-ITS security and misbehaviour detection**. If you use any of the IntelliMD modules, implementations, or ideas in your research or projects, please consider **citing the relevant papers**.  

### 🔗 **Journal Articles**  

1. **Mohamed Ahzam Amanullah, Seng W. Loke, Mohan Baruwal Chhetri, and Robin Doss.**  
   *A Taxonomy and Analysis of Misbehaviour Detection in Cooperative Intelligent Transport Systems: A Systematic Review.*  
   **ACM Computing Surveys**, 56, 1, Article 3 (January 2024), 38 pages.  
   [🔗 DOI: 10.1145/3596598](https://doi.org/10.1145/3596598)  

### 🔗 **Conference Papers**  

1. **Mohamed Ahzam Amanullah, Mohan Baruwal Chhetri, Seng W. Loke, and Robin Doss.**  
   *IntelliMD: A Hybrid Approach for Local Misbehaviour Detection in Cooperative Intelligent Transport Systems.*  
   **CPSIoTSec’24**, October 14–18, 2024, Salt Lake City, UT, USA.  
   **ACM, New York, NY, USA, 12 pages.**  
   [🔗 DOI: 10.1145/3690134.3694817](https://doi.org/10.1145/3690134.3694817)  

2. **Mohamed Ahzam Amanullah, Mohan Baruwal Chhetri, Seng W. Loke, and Robin Doss.**  
   *BurST-ADMA: Towards an Australian Dataset for Misbehaviour Detection in the Internet of Vehicles.*  
   **IEEE PerCom Workshops 2022**, Pisa, Italy, pp. 624-629.  
   [🔗 DOI: 10.1109/PerComWorkshops53856.2022.9767505](https://doi.org/10.1109/PerComWorkshops53856.2022.9767505)  

3. **Anuj Nepal, Mohamed Ahzam Amanullah, Robin Doss, and Frank Jiang.**  
   *Secure Data Provenance in Internet of Vehicles with Data Plausibility for Security and Trust.*  
   **IEEE World AI IoT Congress (AIIoT) 2024**, Seattle, WA, USA, pp. 612-618.  
   [🔗 DOI: 10.1109/AIIoT61789.2024.10578965](https://doi.org/10.1109/AIIoT61789.2024.10578965)  

---
📢 Kindly cite the relevant paper(s) if any module is used or adapted from this work.


## 📜 License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code, provided that proper credit is given to the authors.



