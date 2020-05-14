# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:55:08 2020

@author: Tisana
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 18:26:26 2019

@author: CINO
"""
# set up
from win32com.client import Dispatch
speak=Dispatch("SAPI.SpVoice")
import pandas as pd
import datetime

while True:
    
    print("  ")
    while True:
        x=input("INPUT (y) to record : ")
        file=open('dummy.py','r')
        information=file.read()
        if information=="1":
            print("*********Clear reminder window first*********")
            pass
        elif x=="y":
            break
            
    
    record_file=pd.read_csv("remind.csv")
    
    record_list=[]
    heading_list=[]
    for each_heading in record_file:
        heading_list.append(each_heading)
    record_list.append(heading_list)
    
    for each_list in record_file.values.tolist():
        record_list.append(each_list)
    
    
    
    #add new record
    while True:
        content=input("> WHAT to remind : ")
        if len(content)<35:
            break
        print("Too long")
    
    while True:
        when_to_remind=input("> WHEN to remind : ")
        recorded_time=datetime.datetime.now()
        x=when_to_remind.split()
        #print(x)
        if "next" in x:
            if "day" in x:
                index_of_day=x.index("day")
                index_of_num_day=index_of_day-1
                time_to_remind=datetime.timedelta(days=int(x[index_of_num_day]))
                time_to_remind=recorded_time+time_to_remind
                break
            elif "days" in x:
                index_of_day=x.index("days")
                index_of_num_day=index_of_day-1
                time_to_remind=datetime.timedelta(days=int(x[index_of_num_day]))
                time_to_remind=recorded_time+time_to_remind
                break
            elif "hour" in x:
                index_of_day=x.index("hour")
                index_of_num_day=index_of_day-1
                time_to_remind=datetime.timedelta(hours=int(x[index_of_num_day]))
                time_to_remind=recorded_time+time_to_remind
                break
            elif "hours" in x:
                index_of_day=x.index("hours")
                index_of_num_day=index_of_day-1
                time_to_remind=datetime.timedelta(hours=int(x[index_of_num_day]))
                time_to_remind=recorded_time+time_to_remind
                break
            elif "minute" in x:
                index_of_day=x.index("minute")
                index_of_num_day=index_of_day-1
                time_to_remind=datetime.timedelta(minutes=int(x[index_of_num_day]))
                time_to_remind=recorded_time+time_to_remind
                break
            elif "minutes" in x:
                index_of_day=x.index("minutes")
                index_of_num_day=index_of_day-1
                time_to_remind=datetime.timedelta(minutes=int(x[index_of_num_day]))
                time_to_remind=recorded_time+time_to_remind
                break
            elif "second" in x:
                index_of_day=x.index("second")
                index_of_num_day=index_of_day-1
                time_to_remind=datetime.timedelta(seconds=int(x[index_of_num_day]))
                time_to_remind=recorded_time+time_to_remind
                break
            elif "seconds" in x:
                index_of_day=x.index("seconds")
                index_of_num_day=index_of_day-1
                time_to_remind=datetime.timedelta(seconds=int(x[index_of_num_day]))
                time_to_remind=recorded_time+time_to_remind
                break
        elif "tomorrow" in x:
            time_to_remind=datetime.timedelta(days=1)
            time_to_remind=recorded_time+time_to_remind
            break
            
    print("> recorded at ",recorded_time)
    print("____________________________________________")
    new_record_list=[content,recorded_time,time_to_remind,0]
    record_list.append(new_record_list)
    speak.Speak("recorded")
    
    
    #convert list to data frame
    record_df=pd.DataFrame(record_list)  
    record_df.to_csv("remind.csv",index=False,header=None)


