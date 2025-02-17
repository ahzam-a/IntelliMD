import pandas as pd
from collections import deque
import numpy as np

class RealTimeMedianFilter:
    def __init__(self, window_size=10):
        self.window_size = window_size
        self.window = deque(maxlen=window_size)
    
    def update(self, new_value):
        self.window.append(new_value)
        return np.median(self.window)


df = pd.read_csv("veh531_data.csv")


filters = {
    "sender_x": RealTimeMedianFilter(window_size=10),
    "sender_y": RealTimeMedianFilter(window_size=10),
    "sender_speed": RealTimeMedianFilter(window_size=10),
    "sender_acceleration": RealTimeMedianFilter(window_size=10),
    "sender_heading": RealTimeMedianFilter(window_size=10),
}


df["filtered_sender_x"] = df["sender_x"].apply(filters["sender_x"].update)
df["filtered_sender_y"] = df["sender_y"].apply(filters["sender_y"].update)
df["filtered_sender_speed"] = df["sender_speed"].apply(filters["sender_speed"].update)
df["filtered_sender_acceleration"] = df["sender_acceleration"].apply(filters["sender_acceleration"].update)
df["filtered_sender_heading"] = df["sender_heading"].apply(filters["sender_heading"].update)


df.to_csv("filtered_dataset_531.csv", index=False)
