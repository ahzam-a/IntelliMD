import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    matthews_corrcoef, cohen_kappa_score, classification_report
)
from scipy.stats import norm
from skmultiflow.drift_detection import ADWIN


dataset = pd.read_csv('rsu25.csv')
dataset["label"] = pd.to_numeric(dataset["label"], errors="coerce")
dataset = dataset.fillna(0)


dataset['timestep_diff'] = dataset.groupby('sender_id')['timestep'].diff().fillna(0)
dataset['sender_x_diff'] = dataset.groupby('sender_id')['sender_x'].diff().fillna(0)
dataset['sender_y_diff'] = dataset.groupby('sender_id')['sender_y'].diff().fillna(0)


feature_columns = [
    "timestep", "sender_x", "sender_y", "sender_speed", "sender_heading",
    "inter_arrival_time", "packet_size", "timestep_diff",
    "sender_x_diff", "sender_y_diff"
]
X = dataset[feature_columns].values
y = dataset["label"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42, stratify=y)


rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)


adwin = ADWIN()


predictions = []
window_size = 50
window_errors = []
drift_detected_points = []

for i, (X_sample, y_sample) in enumerate(zip(X_test, y_test)):
    prediction = rf_model.predict([X_sample])[0]
    predictions.append(prediction)
    

    error = int(prediction != y_sample)
    window_errors.append(error)
    adwin.add_element(error)

    if adwin.detected_change():
        print(f"Concept drift detected at index {i}")
        drift_detected_points.append(i)

        rf_model.fit(X_train, y_train)

    if len(window_errors) > window_size:
        window_errors.pop(0)  

