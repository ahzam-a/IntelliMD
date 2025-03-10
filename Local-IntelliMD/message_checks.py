import ast
from curses.panel import new_panel
from xxlimited import new
from haversine import haversine, inverse_haversine, Direction, Unit
import sys,os, json

from importlib_metadata import re

import numpy as np
from pymemcache.client import base
import pandas as pd
client = base.Client(('localhost', 11211))

road_df=pd.read_csv('road_vals.csv')



def beacon_frequency(last_time, new_time):
    if new_time-last_time==1:
        return True
    return False

def comm_range(recv_x, recv_y, sender_x, sender_y):

    distance_range=haversine((recv_y, recv_x), (sender_y,sender_x), unit=Unit.METERS)
    if distance_range<=1000:
        return True
  
    return False

def acceleration_consistency(prev_speed, new_speed, new_acceleration):
    acceleration=new_speed-prev_speed
    if abs(acceleration-new_acceleration)<=0.5:
        return True
    if round(acceleration,2)==round(new_acceleration,2):
        return True
    return False

def acceleration_plausibility(prev_speed, new_speed, new_acceleration):
    new_speed_cal=prev_speed+new_acceleration

    if abs(new_speed_cal-new_speed)<=0.5:
        return True
    if round(new_speed_cal,2)==round(new_speed,2):
        return True
    return False

def speed_consistency(prev_speed, new_speed, new_acceleration):
  
    calc_new_speed=prev_speed+new_acceleration
    if abs(calc_new_speed-new_speed)<=0.5:
        return True
    if round(calc_new_speed,2)==round(new_speed,2):
        return True
    sc_diff.append(new_speed-calc_new_speed)
    return False

def speed_plausibility(speed, prev_speed, new_acc):
    acceleration=speed-prev_speed
    if abs(new_acc-acceleration)<=0.5:
        return True

    if new_acc==acceleration:
        return True
    return False


def position_consistency(prev_x, prev_y, new_x, new_y, dist):

    dist_cal=haversine((prev_y, prev_x), (new_y, new_x), unit=Unit.METERS)

    print(dist_cal)

    if (abs(dist_cal-dist))>1.50:
        print(dist)
        print(dist_cal)
        print(abs(dist_cal-dist))
        return False

    return True


def signal_plausibility(signal, prev_acceleration, new_acceleration, sender_id):
    if signal==3 and new_acceleration<prev_acceleration:
        return True
    return False
    

def trajectory_prediction(prev_x, prev_y, new_x, new_y, prev_angle, distance):

    newcoord=inverse_haversine((prev_y, prev_x), distance, prev_angle, unit=Unit.METERS)

    new_distance=haversine((prev_y, prev_x), (newcoord[0],newcoord[1]), unit=Unit.METERS)

    
    if (abs(new_distance-distance))<=0.01:
        return True
    return False  

length_threshold={'truck_truck':7.1, 'bus_bus':12,'bike_bicycle':1.6,'veh_passenger':5,'pt_bus':12,'motorcycle_motorcycle':2.2,'ped_pedestrian':None, 'pt_bus_bus':12, 'bicycle_bicycle':1.6}
width_threshold={'truck_truck':2.4, 'bus_bus':2.5,'bike_bicycle':0.65,'veh_passenger':1.8,'pt_bus':2.5,'motorcycle_motorcycle':0.9,'ped_pedestrian':None, 'pt_bus_bus':2.5, 'bicycle_bicycle':0.65}

def length_plausibility(length, element_type):
    if length_threshold.get(element_type)==None:
        return True
    elif length==length_threshold[element_type]:
        return True
    elif length<length_threshold[element_type]:
        diff=abs(length/length_threshold[element_type])*100
        if diff>=2:
            return False
        else:
            return True
    return False

def width_plausibility(width, element_type):
    if width_threshold.get(element_type)==None:
        return True
    elif width==width_threshold[element_type]:
        return True
    elif width<width_threshold[element_type]:
        diff=abs(width/width_threshold[element_type])*100
        if diff>=2:
            return False
        else:
            return True
    return False

def type_plausibility(element_type, width, length):
    if 'ped' in element_type:
        return True
    elif element_type in length_threshold.keys() and width<=width_threshold[element_type] and length<=length_threshold[element_type]:
        return True
    return False


def length_consistency(current_length, previous_length):
    if previous_length-current_length==0:
        return True
    return False

def width_consistency(current_width, previous_width):
    if previous_width-current_width==0:
        return True
    return False

def type_consistency(current_type, prev_type):
    if current_type==prev_type:
        return True
    return False

def heading_check(prev_heading, new_heading):
    if new_heading>360 or new_heading<0:
        return False
    if abs(prev_heading-new_heading)>=180:
        return False
    if abs(prev_heading-new_heading) >=0.5:
        return False
    return True

def message_checks(message_type, recv_id, sender_id, timestep, message, prev_data):
    bf=False
    com_range=False
    ac=False
    sc=False
    asc=False
    max_speed=False
    sp=False
    pc=False
    tp=False
    ap=False
    len_p=False
    width_p=False
    type_p=False
    len_c=False
    width_c=False
    type_c=False
    hc=False

    cred_list=[]
    failed=0
    passed=0

    if 'ped' in sender_id:
        bf=beacon_frequency(prev_data['timestep'],message['timestep'])
        com_range=comm_range(prev_data['recv_x'], prev_data['recv_y'], prev_data['sender_x'], prev_data['sender_y'])
        pc=position_consistency(prev_data['sender_x'], prev_data['sender_y'], message['sender_x'], message['sender_y'], message['sender_speed'])
        tp=trajectory_prediction(prev_data['sender_x'], prev_data['sender_y'], message['sender_x'], message['sender_y'], prev_data['sender_angle'], message['sender_speed'])
        type_p=type_plausibility(message['sender_type'], message['sender_width'], message['sender_length'])
        type_c=type_consistency(message['sender_type'], prev_data['sender_type'])
        cred_list=np.array([bf,com_range,pc,tp,type_p,type_c])
        hc=heading_check(prev_data['sender_angle'], message['sender_angle'])
        passed = len([value for value in cred_list if value != False])

    else:
        bf=beacon_frequency(prev_data['timestep'],message['timestep'])
        com_range=comm_range(prev_data['recv_x'], prev_data['recv_y'], prev_data['sender_x'], prev_data['sender_y'])
        ac=acceleration_consistency(prev_data['sender_speed'], message['sender_speed'], message['sender_acceleration'])
        sc=speed_consistency(prev_data['sender_speed'], message['sender_speed'], message['sender_acceleration'])
        asc=acceleration_speed_consistency(prev_data['sender_speed'], message['sender_speed'], message['sender_acceleration'])
        sp=speed_plausibility(message['sender_speed'], prev_data['sender_speed'], message['sender_acceleration'])
        pc=position_consistency(prev_data['sender_x'], prev_data['sender_y'], message['sender_x'], message['sender_y'], message['sender_speed'])
        tp=trajectory_prediction(prev_data['sender_x'], prev_data['sender_y'], message['sender_x'], message['sender_y'], prev_data['sender_angle'], message['sender_speed'])
        ap=acceleration_plausibility(prev_data['sender_speed'], message['sender_speed'], message['sender_acceleration'])
        len_p=length_plausibility(message['sender_length'], message['sender_type'])
        width_p=width_plausibility(message['sender_width'], message['sender_type'])
        type_p=type_plausibility(message['sender_type'], message['sender_width'], message['sender_length'])
        len_c=length_consistency(message['sender_length'], prev_data['sender_length'])
        width_c=width_consistency(message['sender_width'], prev_data['sender_width'])
        type_c=type_consistency(message['sender_type'], prev_data['sender_type'])
        hc=heading_check(prev_data['sender_angle'], message['sender_angle'])
        
        bf=bf
        com_range=com_range
        ac=ac
        sc=sc
        asc=asc
        sp=sp
        pc=pc
        tp=tp
        ap=ap
        len_p=len_p
        width_p=width_p
        type_p=type_p
        len_c=len_c
        width_c=width_c
        type_c=type_c
        hc=hc
        
        cred_list=np.array([bf,com_range,ac,sc,asc,sp,pc,tp,ap,len_p,width_p,type_p,len_c,width_c,type_c, hc])
        
        
        
        failed = len([value for value in cred_list if value != True])
        passed = len([value for value in cred_list if value != False])
        


    message['bf']=bf
    message['com_range']=com_range
    message['ac']=ac
    message['sc']=sc
    message['asc']=asc
    message['sp']=sp
    message['pc']=pc
    message['tp']=tp
    message['ap']=ap
    message['len_p']=len_p
    message['width_p']=width_p
    message['type_p']=type_p
    message['len_c']=len_c
    message['width_c']=width_c
    message['type_c']=type_c
    message['hc']=hc
    
    cred_score=(passed/len(cred_list))*100
    

    message['sc']=sc
    message['cred_score']=cred_score
    
    #after message checks store in cache
    client.set(message_type+'-'+recv_id+'-'+sender_id+'-'+str(timestep), message)
    return message

def check_prev_data(message_type, recv_id, sender_id, timestep, message):
    prev_timestep=timestep-1
    if client.get(message_type+'-'+recv_id+'-'+sender_id+'-'+str(prev_timestep))!=None:
        str_val=client.get(message_type+'-'+recv_id+'-'+sender_id+'-'+str(prev_timestep)).decode("UTF-8")
        try:
            prev_val = ast.literal_eval(str_val)
        except Exception as e:
            prev_val={}
        return prev_val
    else:
        return {}
    
def lane_check(road, sender_lane):
    if road in road_df['road']:
        num_lanes=road_df.loc[(road_df['road'] == road)]['lanes']
        if sender_lane<=num_lanes:
            return True
        return False
    return False

def braking_check(signal, prev_speed, new_speed):
    if signal==3 and prev_speed>new_speed:
        return True
    return False


convert_list=list()

import pandas as pd
import time 
from psutil import cpu_percent

msg_list=list()
def main():
    df=pd.DataFrame()

    msg_count=0

    data_csv=pd.read_csv('veh513_data.csv')
    data_csv['type']='BSM'
    data_csv=data_csv.rename(columns={"sender_veh_type": "sender_type", "sender_heading": "sender_angle"})
    
    data_csv=data_csv.rename(columns={"pos_noisy_x_cleaned": "sender_x", 
    "pos_noisy_y_cleaned": "sender_y",
    "speed_noisy_cleaned": "sender_speed",
    "length_noisy_cleaned": "sender_length",
    "width_noisy_cleaned": "sender_width",
    "heading_noisy_cleaned": "sender_angle",
    "acceleration_noisy_cleaned": "sender_acceleration"

    }) 
    
    data_json=data_csv.to_dict(orient='records')
    consumer = data_json

    bf=cpu_percent()

    

    for message in consumer:
        msg_count=msg_count+1
        start_t=time.time()
   
        dict_val=message

        if dict_val['type']=='BSM':
            
            prev_data=check_prev_data('BSM', dict_val['recv_id'], dict_val['sender_id'], dict_val['timestep'], dict_val)
            
            
            if len(prev_data)>0:
                if 'rsu' not in element:
                    checked_message=message_checks('BSM', dict_val['recv_id'], dict_val['sender_id'], dict_val['timestep'], dict_val, prev_data)
                    checked_message['cpu']=abs(bf-cpu_percent())
                    print("sender: ", checked_message['sender_id'], "credibility score: ", checked_message['cred_score'], "label: ", checked_message['label'])
            
                    checked_message['det_time']=time.time()-start_t
            
                    convert_list.append(checked_message)
     
            else:

                convert_list.append(dict_val)
                client.set('BSM'+'-'+dict_val['recv_id']+'-'+dict_val['sender_id']+'-'+str(dict_val['timestep']), dict_val)

            
            
     
        elif dict_val['type']=='DENM':
            client.set(dict_val['type']+'-'+str(dict_val['timestep'])+'-'+dict_val['recv_id'], dict_val)

    
    new_df=pd.DataFrame(convert_list)
    new_df.to_csv('accuracy-veh531.csv')
          


if __name__ == "__main__":
    main()
    