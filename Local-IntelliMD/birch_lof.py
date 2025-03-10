import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import LocalOutlierFactor
from sklearn.cluster import Birch

def real_time_hybrid_detection_birch_lof(file_path, output_path):

    data = pd.read_csv(file_path)
    data = data.rename(columns={
        "pos_noisy_x_cleaned": "sender_x", 
        "pos_noisy_y_cleaned": "sender_y",
        "speed_noisy_cleaned": "sender_speed",
        "heading_noisy_cleaned": "sender_angle",
        "acceleration_noisy_cleaned": "sender_acceleration"
    })
    

    features = ["sender_x", "sender_y", "sender_heading", "inter_arrival_time", "packet_size"]

    target = "label"
    data = data.dropna(subset=features + [target])
    

    scaler = StandardScaler()
    pca = PCA(n_components=4)
    birch = Birch(n_clusters=None, threshold=0.7, branching_factor=50)
    lof = LocalOutlierFactor(n_neighbors=20, novelty=True, contamination=0.35, metric='jaccard')  # LOF


    X = data[features]
    y = data[target]
    y_binary = np.where(y == 0, 0, 1)
    X_scaled = scaler.fit_transform(X)
    X_pca = pca.fit_transform(X_scaled)
    

    birch.fit(X_pca)
    lof.fit(X_pca)


    true_positives, true_negatives, false_positives, false_negatives = 0, 0, 0, 0
    predictions = []


    for i in range(len(X_scaled)):
        record = X_scaled[i].reshape(1, -1)  
        record_pca = pca.transform(record)  
        
        birch_label = birch.predict(record_pca)
        birch_binary = 1 if birch_label != 0 else 0
        
        
        lof_label = lof.predict(record_pca)
        lof_binary = 1 if lof_label == -1 else 0
        
        
        final_label = 1 if (birch_binary + lof_binary) > 0 else 0
        predictions.append(final_label)
        
        
        actual_label = y_binary[i]
        
        
        if final_label == 1 and actual_label == 1:
            true_positives += 1
        elif final_label == 0 and actual_label == 0:
            true_negatives += 1
        elif final_label == 1 and actual_label == 0:
            false_positives += 1
        elif final_label == 0 and actual_label == 1:
            false_negatives += 1
        
        
        print(f"Record {i+1}/{len(X_scaled)} - Predicted: {final_label}, Actual: {actual_label}")

    
    data['anomaly_prediction'] = predictions

    
    data.to_csv(output_path, index=False)
    print(f"\nPredictions saved to {output_path}")

    
file_path = 'veh531_data.csv'  
output_path = 'accuracy_with_predictions.csv' 
real_time_hybrid_detection_birch_lof(file_path, output_path)
