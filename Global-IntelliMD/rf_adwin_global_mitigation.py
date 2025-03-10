import pandas as pd
import numpy as np
import psutil 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from scipy.stats import norm
from skmultiflow.drift_detection import ADWIN
from collections import defaultdict
import time



dataset = pd.read_csv('filtered_senders_with_rsu15.csv').sample(frac=0.1, random_state=42)
dataset["label"] = pd.to_numeric(dataset["label"], errors="coerce")
dataset = dataset.fillna(0)
dataset = dataset.rename(columns={
    "pos_noisy_x_cleaned": "sender_x",
    "pos_noisy_y_cleaned": "sender_y",
    "speed_noisy_cleaned": "sender_speed",
    "heading_noisy_cleaned": "sender_heading",
    "acceleration_noisy_cleaned": "sender_acceleration"
})


feature_columns = ["timestep", "recv_x", "recv_y", "sender_x", "sender_y", "sender_speed", 
                   "sender_acceleration", "sender_heading", "inter_arrival_time", "packet_size"]
label_column = 'label'


X = dataset[feature_columns].values
y = dataset[label_column]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)



rf_model = RandomForestClassifier()



train_start = time.time()
rf_model.fit(X_train, y_train)  
train_end = time.time()


adwin = ADWIN()


sender_warnings = defaultdict(int)
classification_results = []

ignored_rsus = set()

for i, (X_sample, y_sample) in enumerate(zip(X_test, y_test)):

    prediction = rf_model.predict([X_sample])[0]


    true_label = dataset.iloc[i]['classification_label']


    sender_id = dataset.iloc[i]['sender_id']
    rsu_id = dataset.iloc[i]['rsu_id']


    if prediction != true_label:
        ignored_rsus.add(rsu_id)  
        print(f"RSU {rsu_id} will be removed from the network due to incorrect classification for sender {sender_id}")


    if 1 <= prediction <= 19:
        sender_warnings[sender_id] += 1
        if sender_warnings[sender_id] == 1:
            print(f"Warning: Potential misbehavior detected for sender {sender_id} (Label: {prediction})")
        elif sender_warnings[sender_id] >= 2:  
            print(f"Certificate Revocation Message: Sender {sender_id} triggered multiple warnings (Label: {prediction})")

    elif 20 <= prediction <= 22:
        print(f"Immediate Certificate Revocation Message: Critical attack detected for sender {sender_id} (Label: {prediction})")


    error = int(prediction != y_sample)
    adwin.add_element(error)
    if adwin.detected_change():
        print(f"Concept drift detected at record {i}. Re-training the model.")
        rf_model.fit(X_train, y_train) 


