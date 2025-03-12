import pandas as pd
import numpy as np
from haversine import haversine, Unit

import numpy as np

main_df=pd.read_csv('accuracy_with_predictions.csv')

com_df=pd.read_csv('com.csv')


position_checks=['pc', 'tp']
acceleration_checks=['ac', 'asc', 'ap']
speed_checks=['sc', 'sp']
heading_checks=['hc']
len_checks=['len_p','len_c']
width_checks=['width_p', 'width_c']
type_checks=['type_p', 'type_c']
frequency_checks=['bf']
range_checks=['com_range']


thresholding={
    'position':0,
    'acceleration':0,
    'speed':0,
    'heading':0,
    'length':0,
    'width':0,
    'frequency':0,
    'range':1000,
}


def adaptive_thresholding():

    get_neighbours=com_df.loc[(com_df['observee_id']==row['sender_id']) & (com_df['timestep']==row['timestep'])]


    pos_neighbours=com_df.loc[(com_df['observee_id']==row['sender_id']) & (com_df['timestep']==row['timestep'])][['observer_x','observer_y']].mean()


    com_df.loc[(com_df['observee_id']==row['sender_id']) & (com_df['timestep']==row['timestep'])][['observer_y']]-row['sender_y']



def confidence_scoring_system(sender_id):
    sender_data=pd.DataFrame(past_history[row['sender_id']])
    score=sender_data['cred_score'].mean()


    return score

past_history=dict()
main_df = main_df.fillna(0)
new_main_df=main_df
current_recv='veh513'
main_df=main_df.loc[main_df['recv_id']==current_recv]
nodes_scoring=dict()


import statistics

length_threshold={'truck_truck':7.1, 'bus_bus':12,'bike_bicycle':1.6,'veh_passenger':5,'pt_bus':12,'moto_motorcycle':2.2,'ped_pedestrian':None}
width_threshold={'truck_truck':2.4, 'bus_bus':2.5,'bike_bicycle':0.65,'veh_passenger':1.8,'pt_bus':2.5,'moto_motorcycle':0.9,'ped_pedestrian':None}


def validate_pos(sender_id, timestep,sender_x, sender_y, neighbours, lmd_res):


    neighbour_list=list(get_neighbours['observer_id'])
    if current_recv in neighbour_list:
        neighbour_list.remove(current_recv)


    x_values=list()
    y_values=list()


    
    for i in neighbour_list:
        
        data=new_main_df.loc[(new_main_df['sender_id']==i) & (new_main_df['timestep']<=timestep)]['cred_score'].mean()


        if credibility_scoring.get(i)==None and data>=90:
            x_values.append(get_neighbours.loc[(get_neighbours['observer_id']==i)]['observer_x'].iloc[0])
            y_values.append(get_neighbours.loc[(get_neighbours['observer_id']==i)]['observer_y'].iloc[0])


        
        elif credibility_scoring.get(i)==None and data<90:
            return True


        elif credibility_scoring.get(i)==None:
                continue


        
        elif credibility_scoring.get(i)>90:
            x_val=get_neighbours.loc[(get_neighbours['observer_id']==i)]['observer_x'].iloc[0]
            y_val=get_neighbours.loc[(get_neighbours['observer_id']==i)]['observer_y'].iloc[0]


            x_values.append(x_val)
            y_values.append(y_val)


            
    if len(x_values)==0:
        return lmd_res
    if len(y_values)==0:
        return lmd_res


    x_mean=statistics.mean(x_values)
    y_mean=statistics.mean(y_values)


            
    if sender_x<=x_mean and sender_y<=y_mean:
        return lmd_res
    else:
        return True
    




def validate_speed(sender_id, timestep,sender_speed, neighbours, lmd_res):
    
    neighbour_list=list(get_neighbours['observer_id'])
    if current_recv in neighbour_list:
        neighbour_list.remove(current_recv)
    speed_values=list()


    
    for i in neighbour_list:
        
        data=new_main_df.loc[(new_main_df['sender_id']==i)& (new_main_df['timestep']<=timestep)]['cred_score'].mean()


        if credibility_scoring.get(i)==None and data>=90:
            speed_values.append(get_neighbours.loc[(get_neighbours['observer_id']==i)]['observer_speed'].iloc[0])
        
    
        elif credibility_scoring.get(i)==None and data<90:
            return True


        elif credibility_scoring.get(i)==None:
                continue


    
        elif credibility_scoring.get(i)>90:
            speed_values.append(get_neighbours.loc[(get_neighbours['observer_id']==i)]['observer_speed'].iloc[0])
            
            


    if len(speed_values)==0:
        return lmd_res


    speed_mean=statistics.mean(speed_values)
    


    if sender_speed<=speed_mean:
        return lmd_res
    else:
        return True


def validate_acceleration(sender_id, timestep,sender_acceleration, neighbours, lmd_res):


    
    neighbour_list=list(get_neighbours['observer_id'])
    if current_recv in neighbour_list:
        neighbour_list.remove(current_recv)


    acc_values=list()


    
    for i in neighbour_list:
        
        data=new_main_df.loc[(new_main_df['sender_id']==i) & (new_main_df['timestep']<=timestep)]['cred_score'].mean()


        if credibility_scoring.get(i)==None and data>=90:
            acc_values.append(get_neighbours.loc[(get_neighbours['observer_id']==i)]['observer_acceleration'].iloc[0])
        
        
        elif credibility_scoring.get(i)==None and data<90:
            return True
        
        elif credibility_scoring.get(i)==None:
                continue


        
        elif credibility_scoring.get(i)>90:
            acc_values.append(get_neighbours.loc[(get_neighbours['observer_id']==i)]['observer_acceleration'].iloc[0])
            


            
    if len(acc_values)==0:
        return lmd_res
      
    acc_mean=statistics.mean(acc_values)
    


    if sender_acceleration<=acc_mean:
        return lmd_res
    else:
        return True
    


def validate_heading(sender_id, timestep,sender_heading, neighbours, lmd_res):
    
    neighbour_list=list(get_neighbours['observer_id'])
    if current_recv in neighbour_list:
        neighbour_list.remove(current_recv)
    heading_values=list()


    
    for i in neighbour_list:
        
        data=new_main_df.loc[(new_main_df['sender_id']==i) & (new_main_df['timestep']<=timestep)]['cred_score'].mean()


        if credibility_scoring.get(i)==None and data>=90:
            heading_values.append(get_neighbours.loc[(get_neighbours['observer_id']==i)]['observer_angle'].iloc[0])
        
        
        elif credibility_scoring.get(i)==None and data<90:
            return True


        elif credibility_scoring.get(i)==None:
                continue


        
        elif credibility_scoring.get(i)>90:
            heading_values.append(get_neighbours.loc[(get_neighbours['observer_id']==i)]['observer_angle'].iloc[0])
            
            


    if len(heading_values)==0:
        return lmd_res


    heading_mean=statistics.mean(heading_values)
    


    if sender_heading<=heading_mean:
        return lmd_res
    else:
        return True


def validate_length(sender_id, timestep,sender_length, neighbours, lmd_res):
    
    neighbour_list=list(get_neighbours['observer_id'])
    if current_recv in neighbour_list:
        neighbour_list.remove(current_recv)


    length_values=list()


    
    for i in neighbour_list:
        
        data=new_main_df.loc[(new_main_df['sender_id']==i) & (new_main_df['timestep']<=timestep)]['cred_score'].mean()


        if credibility_scoring.get(i)==None and data>=90:
            length_values.append(get_neighbours.loc[(get_neighbours['observer_id']==i)]['observer_length'].iloc[0])
        
    
        elif credibility_scoring.get(i)==None and data<90:
            return True


        elif credibility_scoring.get(i)==None:
                continue


    
        elif credibility_scoring.get(i)>90:
            length_values.append(get_neighbours.loc[(get_neighbours['observer_id']==i)]['observer_length'].iloc[0])
            
            


    if len(length_values)==0:
        return lmd_res


    length_mean=statistics.mean(length_values)
    


    if abs(statistics.mean(length_values)-row['sender_length'])<=0.2:
        return lmd_res
    else:
        return True


def validate_width(sender_id, timestep,sender_width, neighbours, lmd_res):
    
    neighbour_list=list(get_neighbours['observer_id'])
    if current_recv in neighbour_list:
        neighbour_list.remove(current_recv)


    width_values=list()


    
    for i in neighbour_list:
    
        data=new_main_df.loc[(new_main_df['sender_id']==i) & (new_main_df['timestep']<=timestep)]['cred_score'].mean()


        if credibility_scoring.get(i)==None and data>=90:
            width_values.append(get_neighbours.loc[(get_neighbours['observer_id']==i)]['observer_width'].iloc[0])
        
    
        elif credibility_scoring.get(i)==None and data<90:
            return True


        elif credibility_scoring.get(i)==None:
            continue
    
        elif credibility_scoring.get(i)>90:
            width_values.append(get_neighbours.loc[(get_neighbours['observer_id']==i)]['observer_width'].iloc[0])
            
            


    if len(width_values)==0:
        return lmd_res
    width_mean=statistics.mean(width_values)
    


    if sender_width<=width_mean:
        return lmd_res
    else:
        return True


def validate_type(sender_id, timestep,sender_type, sender_length, sender_width, neighbours, lmd_res):
    
    neighbour_list=list(get_neighbours['observer_id'])
    if current_recv in neighbour_list:
        neighbour_list.remove(current_recv)
    len_res=validate_length(sender_id, timestep,sender_length, neighbours, lmd_res)
    width_res=validate_width(sender_id, timestep,sender_width, neighbours, lmd_res)


    if len_res==True and width_res==True:
        type_values=list()


    
        for i in neighbour_list:
    
            data=new_main_df.loc[(new_main_df['sender_id']==i) & (new_main_df['timestep']<=timestep)]['cred_score'].mean()


            if credibility_scoring.get(i)==None and data>=90:
                type_values.append(get_neighbours.loc[(get_neighbours['observer_id']==i)]['observer_type'].iloc[0])
            
    
            elif credibility_scoring.get(i)==None and data<90:
                return True


            elif credibility_scoring.get(i)==None:
                continue
    
            elif credibility_scoring.get(i)>90:
                type_values.append(get_neighbours.loc[(get_neighbours['observer_id']==i)]['observer_type'].iloc[0])
                
                


        if len(type_values)==0:
            return lmd_res


        type_median=statistics.mode(type_values)
        


        if sender_type==type_median:
            return lmd_res
        else:
            return True
    else:
        return True
        


def validate_lane_pos(timestep, lane_pos):
    
    neighbour_list = list(get_neighbours['observer_id'])
    if current_recv in neighbour_list:
        neighbour_list.remove(current_recv)

    lane_values = []

    
    for i in neighbour_list:
    
        data = new_main_df.loc[
            (new_main_df['sender_id'] == i) & (new_main_df['timestep'] <= timestep)
        ]['cred_score'].mean()

        if credibility_scoring.get(i) is None and data >= 90:
            lane_values.append(
                get_neighbours.loc[
                    get_neighbours['observer_id'] == i
                ]['observed_lane_pos'].iloc[0]
            )

    
        elif credibility_scoring.get(i) is None and data < 90:
            return True

        elif credibility_scoring.get(i) is None:
            continue

    
        elif credibility_scoring.get(i) > 90:
            credibility_scoring.append(
                get_neighbours.loc[
                    get_neighbours['observer_id'] == i
                ]['observed_lane_pos'].iloc[0]
            )

    if len(lane_values) == 0:
        return lane_pos  

    
    lane_mode_new = statistics.mode(lane_values)

    if lane_pos==lane_mode_new:
            return False
    else:
            return True




    
def validate_event_type(timestep, event_type):
    
    neighbour_list = list(get_neighbours['observer_id'])
    if current_recv in neighbour_list:
        neighbour_list.remove(current_recv)

    neigh_values = []

    
    for i in neighbour_list:
    
        data = new_main_df.loc[
            (new_main_df['sender_id'] == i) & (new_main_df['timestep'] <= timestep)
        ]['cred_score'].mean()

        if credibility_scoring.get(i) is None and data >= 90:
            neigh_values.append(
                get_neighbours.loc[
                    get_neighbours['observer_id'] == i
                ]['event_type'].iloc[0]
            )

    
        elif credibility_scoring.get(i) is None and data < 90:
            return True

        elif credibility_scoring.get(i) is None:
            continue

    
        elif credibility_scoring.get(i) > 90:
            credibility_scoring.append(
                get_neighbours.loc[
                    get_neighbours['observer_id'] == i
                ]['event_type'].iloc[0]
            )

    if len(neigh_values) == 0:
        return event_type  

    
    event_type_new = statistics.mode(neigh_values)
    

    if event_type==event_type_new:
            return False
    else:
            return True
    
def validate_cause_code(timestep, cause_code):
    
    neighbour_list = list(get_neighbours['observer_id'])
    if current_recv in neighbour_list:
        neighbour_list.remove(current_recv)

    neigh_values = []

    
    for i in neighbour_list:
    
        data = new_main_df.loc[
            (new_main_df['sender_id'] == i) & (new_main_df['timestep'] <= timestep)
        ]['cred_score'].mean()

        if credibility_scoring.get(i) is None and data >= 90:
            neigh_values.append(
                get_neighbours.loc[
                    get_neighbours['observer_id'] == i
                ]['cause_code'].iloc[0]
            )

    
        elif credibility_scoring.get(i) is None and data < 90:
            return True

        elif credibility_scoring.get(i) is None:
            continue

    
        elif credibility_scoring.get(i) > 90:
            credibility_scoring.append(
                get_neighbours.loc[
                    get_neighbours['observer_id'] == i
                ]['cause_code'].iloc[0]
            )

    if len(neigh_values) == 0:
        return cause_code  

    
    cause_code_new = statistics.mode(neigh_values)
    

    if cause_code==cause_code_new:
            return False
    else:
            return True
    
def validate_lanes_controlled(timestep, lane_controlled):
            
    neighbour_list = list(get_neighbours['observer_id'])
    if current_recv in neighbour_list:
        neighbour_list.remove(current_recv)

    neigh_values = []

    
    for i in neighbour_list:
        
        data = new_main_df.loc[
            (new_main_df['sender_id'] == i) & (new_main_df['timestep'] <= timestep)
        ]['cred_score'].mean()

        if credibility_scoring.get(i) is None and data >= 90:
            neigh_values.append(
                get_neighbours.loc[
                    get_neighbours['observer_id'] == i
                ]['lane_controlled'].iloc[0]
            )

        
        elif credibility_scoring.get(i) is None and data < 90:
            return True

        elif credibility_scoring.get(i) is None:
            continue

        
        elif credibility_scoring.get(i) > 90:
            credibility_scoring.append(
                get_neighbours.loc[
                    get_neighbours['observer_id'] == i
                ]['lane_controlled'].iloc[0]
            )

    if len(neigh_values) == 0:
        return lane_controlled  

    
    lane_controlled_new = statistics.mode(neigh_values)
    

    if lane_controlled==lane_controlled_new:
            return False
    else:
            return True
    
def validate_lane_signal(timestep, lane_signal):
            # List of neighbours
    neighbour_list = list(get_neighbours['observer_id'])
    if current_recv in neighbour_list:
        neighbour_list.remove(current_recv)

    neigh_values = []

    
    for i in neighbour_list:
    
        data = new_main_df.loc[
            (new_main_df['sender_id'] == i) & (new_main_df['timestep'] <= timestep)
        ]['cred_score'].mean()

        if credibility_scoring.get(i) is None and data >= 90:
            neigh_values.append(
                get_neighbours.loc[
                    get_neighbours['observer_id'] == i
                ]['lane_signal'].iloc[0]
            )

    
        elif credibility_scoring.get(i) is None and data < 90:
            return True

        elif credibility_scoring.get(i) is None:
            continue

    
        elif credibility_scoring.get(i) > 90:
            credibility_scoring.append(
                get_neighbours.loc[
                    get_neighbours['observer_id'] == i
                ]['lane_signal'].iloc[0]
            )

    if len(neigh_values) == 0:
        return lane_signal  

    
    lane_signal_new = statistics.mode(neigh_values)
    

    if lane_signal==lane_signal_new:
            return False
    else:
            return True
    

def validate_signal_remaining_time(timestep, remaining_time):
            
    neighbour_list = list(get_neighbours['observer_id'])
    if current_recv in neighbour_list:
        neighbour_list.remove(current_recv)

    neigh_values = []

    
    for i in neighbour_list:
        
        data = new_main_df.loc[
            (new_main_df['sender_id'] == i) & (new_main_df['timestep'] <= timestep)
        ]['cred_score'].mean()

        if credibility_scoring.get(i) is None and data >= 90:
            neigh_values.append(
                get_neighbours.loc[
                    get_neighbours['observer_id'] == i
                ]['remaining_time'].iloc[0]
            )

    
        elif credibility_scoring.get(i) is None and data < 90:
            return True

        elif credibility_scoring.get(i) is None:
            continue

    
        elif credibility_scoring.get(i) > 90:
            credibility_scoring.append(
                get_neighbours.loc[
                    get_neighbours['observer_id'] == i
                ]['remaining_time'].iloc[0]
            )

    if len(neigh_values) == 0:
        return remaining_time  

    
    remaining_time_new = statistics.mode(neigh_values)
    


    if remaining_time==remaining_time_new:
            return False
    else:
            return True

def validate_lane_disallowed(timestep, lane_disallowed):
    
    neighbour_list = list(get_neighbours['observer_id'])
    if current_recv in neighbour_list:
        neighbour_list.remove(current_recv)

    neigh_values = []

    
    for i in neighbour_list:
        
        data = new_main_df.loc[
            (new_main_df['sender_id'] == i) & (new_main_df['timestep'] <= timestep)
        ]['cred_score'].mean()

        if credibility_scoring.get(i) is None and data >= 90:
            observer_speed = get_neighbours.loc[
                get_neighbours['observer_id'] == i
            ]['lane_disallowed'].iloc[0]

        
            neigh_values.append(observer_speed)

        
        elif credibility_scoring.get(i) is None and data < 90:
            return True

        elif credibility_scoring.get(i) is None:
            continue

    
        elif credibility_scoring.get(i) > 90:
            observer_speed = get_neighbours.loc[
                get_neighbours['observer_id'] == i
            ]['lane_disallowed'].iloc[0]

    
            neigh_values.append(lane_disallowed)

    
    if len(neigh_values) == 0:
        return lane_disallowed  

    
    lane_disallowed_new = statistics.mode(neigh_values)

    if lane_disallowed==lane_disallowed_new:
            return False
    else:
            return True

def validate_lane_length(timestep, lane_length):
    
    neighbour_list = list(get_neighbours['observer_id'])
    if current_recv in neighbour_list:
        neighbour_list.remove(current_recv)

    neigh_values = []

    
    for i in neighbour_list:
    
        data = new_main_df.loc[
            (new_main_df['sender_id'] == i) & (new_main_df['timestep'] <= timestep)
        ]['cred_score'].mean()

        if credibility_scoring.get(i) is None and data >= 90:
            neigh_values.append(
                get_neighbours.loc[
                    get_neighbours['observer_id'] == i
                ]['lane_length'].iloc[0]
            )

        
        elif credibility_scoring.get(i) is None and data < 90:
            return True

        elif credibility_scoring.get(i) is None:
            continue

        
        elif credibility_scoring.get(i) > 90:
            credibility_scoring.append(
                get_neighbours.loc[
                    get_neighbours['observer_id'] == i
                ]['lane_length'].iloc[0]
            )

    if len(neigh_values) == 0:
        return lane_length  


    lane_length_new = statistics.mean(neigh_values)
    

    if lane_length<=lane_length_new:
            return False
    else:
            return True

def validate_speed_limit(timestep, speed_limit):
                
    neighbour_list = list(get_neighbours['observer_id'])
    if current_recv in neighbour_list:
        neighbour_list.remove(current_recv)

    neigh_values = []


    for i in neighbour_list:

        data = new_main_df.loc[
            (new_main_df['sender_id'] == i) & (new_main_df['timestep'] <= timestep)
        ]['cred_score'].mean()

        if credibility_scoring.get(i) is None and data >= 90:
            neigh_values.append(
                get_neighbours.loc[
                    get_neighbours['observer_id'] == i
                ]['observed speed limit'].iloc[0]
            )


        elif credibility_scoring.get(i) is None and data < 90:
            return True

        elif credibility_scoring.get(i) is None:
            continue


        elif credibility_scoring.get(i) > 90:
            credibility_scoring.append(
                get_neighbours.loc[
                    get_neighbours['observer_id'] == i
                ]['observed speed limit'].iloc[0]
            )

    if len(neigh_values) == 0:
        return speed_limit  


    speed_limit_new = statistics.mean(neigh_values)

        

    if speed_limit<=speed_limit_new:
            return False
    else:
            return True
    


final_df=pd.DataFrame()


credibility_scoring=dict()




for index, row in main_df.iterrows():
  
  misb_checker=list()


  get_neighbours=com_df.loc[(com_df['observee_id']==row['sender_id']) & (com_df['timestep']==row['timestep'])]
  row['misb']=False
 

   
  if row['sender_id'] in credibility_scoring:
    
    
    current_cred=row['cred_score']
    prev_cred=credibility_scoring[row['sender_id']]


    
    if np.isnan(row['cred_score']) : current_cred=100 
    if np.isnan(credibility_scoring[row['sender_id']]): prev_cred=100


    
    if current_cred==0 or prev_cred==0: credibility_scoring[row['sender_id']]= prev_cred+current_cred
    else: credibility_scoring[row['sender_id']]=(prev_cred+current_cred)/2


  else:
    
    credibility_scoring[row['sender_id']]=row['cred_score']

  if row['type']=='IVIM':
      if len(get_neighbours)>0:
            res1=validate_lane_disallowed(row['timestep'], row['lane_disallowed'])
            res2=validate_lane_length(row['timestep'], row['lane_length'])
            res3=validate_lane_disallowed(row['timestep'], row['lane_disallowed'])
    
            misb_checker.append(res1)
            misb_checker.append(res2)
            misb_checker.append(res3)
      else:
    
            row['misb_pos']=False
            row['misb']=False
            misb_checker.append(False)
    
      if False in misb_checker and True in misb_checker:
            row['misb']=True
    
      final_df = pd.concat([final_df, pd.DataFrame([row])], ignore_index=True)
      continue


  if row['type']=='SPAT':
      if len(get_neighbours)>0:
            res1=validate_signal_remaining_time(row['timestep'], row['remaining_time'])
            res2=validate_lane_signal(row['timestep'], row['lane_signal'])
            res3=validate_lanes_controlled(row['timestep'], row['lane_controlled'])
            misb_checker.append(res1)
            misb_checker.append(res2)
            misb_checker.append(res3)
      else:
    
            row['misb_pos']=False
            row['misb']=False
            misb_checker.append(False)
    
      if False in misb_checker and True in misb_checker:
            row['misb']=True
    
      final_df = pd.concat([final_df, pd.DataFrame([row])], ignore_index=True)
      continue
      

  if row['type']=='DENM':
      
      

      if len(get_neighbours)>0:
            res1=validate_event_type(row['timestep'], row['event_type'])
            res2=validate_cause_code(row['timestep'], row['cause_code'])
            misb_checker.append(res1)
            misb_checker.append(res2)
      else:
    
            row['misb_pos']=False
            row['misb']=False
            misb_checker.append(False)
    
      if False in misb_checker and True in misb_checker:
            row['misb']=True
    
      final_df = pd.concat([final_df, pd.DataFrame([row])], ignore_index=True)
      continue

  

  
  if ~np.isnan(row['cred_score']) and row['cred_score']<100.0 and row['cred_score']!=0:




    if row['cred_score']<100: lmd_res=True 
    else: lmd_res=False
  
    if row['tp']==False or row['pc']==False:
        if len(get_neighbours)>0:
            res=validate_pos(row['sender_id'], row['timestep'],row['sender_x'], row['sender_y'], get_neighbours, lmd_res)
            row['misb_pos']=res
            row['misb']=res
            misb_checker.append(res)
        else:
        
            row['misb_pos']=True
            row['misb']=True
            misb_checker.append(True)
    
    
    if row['ac']==False or row['asc']==False or row['ap']==False:
        if len(get_neighbours)>0:
    
            res=validate_acceleration(row['sender_id'], row['timestep'],row['sender_acceleration'], get_neighbours, lmd_res)
            row['misb_acc']=res
            row['misb']=res
            misb_checker.append(res)
        else:
    
            row['misb_acc']=True
            row['misb']=True
            misb_checker.append(True)
    
    if row['sc']==False or row['sp']==False:
        if len(get_neighbours)>0:
            res=validate_speed(row['sender_id'], row['timestep'],row['sender_speed'], get_neighbours, lmd_res)
            row['misb_speed']=res
            row['misb']=res
            misb_checker.append(res)
        else:
    
            row['_speed']=True
            row['misb']=True
            misb_checker.append(True)
    
    if row['hc']==False:
        if len(get_neighbours)>0:
            res=validate_heading(row['sender_id'], row['timestep'],row['sender_angle'], get_neighbours, lmd_res)
            row['misb_heading']=res
            row['misb']=res
            misb_checker.append(res)
        else:
    
            row['misb_heading']=True
            row['misb']=True
            misb_checker.append(True)
    
    if row['len_p']==False or row['len_c']==False:
        if len(get_neighbours)>0:
            res=validate_length(row['sender_id'], row['timestep'],row['sender_length'], get_neighbours, lmd_res)
            row['misb_len']=res
            row['misb']=res
            misb_checker.append(res)
      
    
        else:
            
            row['misb_len']=True
            row['misb']=True
            misb_checker.append(True)
       
    
    if row['width_p']==False or row['width_c']==False:
        if len(get_neighbours)>0:
            res=validate_width(row['sender_id'], row['timestep'],row['sender_width'], get_neighbours, lmd_res)
            row['misb_width']=res
            row['misb']=res
            misb_checker.append(res)
     
        else:
    
            row['misb_width']=True
            row['misb']=True
            misb_checker.append(True)
           
    
    if row['type_p']==False or row['type_c']==False:
        if len(get_neighbours)>0:
            res=validate_type(row['sender_id'], row['timestep'],row['sender_type'],row['sender_length'],row['sender_width'], get_neighbours, lmd_res)
            row['misb_type']=res
            row['misb']=res
            misb_checker.append(res)
            
        else:
            
            row['misb_type']=True
            row['misb']=True
            misb_checker.append(True)

            


    
    if False in misb_checker and True in misb_checker:
        row['misb']=True
    
   


    final_df = pd.concat([final_df, pd.DataFrame([row])], ignore_index=True)

    


