# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:54:31 2020

@author: Tisana
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:37:34 2019

@author: CINO
"""
import winsound
from win32com.client import Dispatch
speak=Dispatch("SAPI.SpVoice")
import pandas as pd
import datetime
import time
speak.Speak("Ready")
i=0
between_file=open('dummy.py','w')
between_file.write("0")
between_file.close()
while True:
    
    
    #record_list=record_file.values.tolist()
    i=i+1
    if i==1:
        print("\r"," \  ",end="")
        time.sleep(0.15)


    elif i==2:
        print("\r"," /  ",end="")
        time.sleep(0.15)
    elif i==3:
        print("\r"," -  ",end="")
        time.sleep(0.15)
        i=0
    timenow=datetime.datetime.now()
    
    
    record_file=pd.read_csv("remind.csv")

    record_list=[]
    heading_list=[]
    for each_heading in record_file:
        heading_list.append(each_heading)
    record_list.append(heading_list)
    
    for each_list in record_file.values.tolist():
        record_list.append(each_list)
    #print(record_file)   
    skip_heading=0
    for each_list in record_list:
        skip_heading=skip_heading+1
        if skip_heading==1:
            pass
        elif each_list[3]==0 and timenow>=datetime.datetime.strptime(each_list[2],"%Y-%m-%d %H:%M:%S.%f"):
            winsound.Beep(400,700)
            print("\r","        ")
            print("REMINDER ALERT !!!!!! ")
            #print("================================================")
            print("> ",each_list[0])
            #print("================================================")
            #speak.Speak("Reminder alert : ")
            speak.Speak(each_list[0])
            remind_to_speak=each_list[0]
            #speak.Speak("Snooze or mark as complete ?")
            
            between_file=open('between_remind_and_record.py','w')
            between_file.write("1")
            between_file.close()
            next_command=input(">  Snooze / Mark as complete : ")
            between_file=open('between_remind_and_record.py','w')
            between_file.write("0")
            between_file.close()
            
            x=next_command.split()
            if "remind" in x or "snooze" in x or "next" in x:
                timenow=datetime.datetime.now()
                if "snooze" in x:
                    time_to_remind=datetime.timedelta(minutes=15)
                    time_to_remind=timenow+time_to_remind
                elif "day" in x:
                    index_of_day=x.index("day")
                    index_of_num_day=index_of_day-1
                    time_to_remind=datetime.timedelta(days=int(x[index_of_num_day]))
                    time_to_remind=timenow+time_to_remind
                elif "days" in x:
                    index_of_day=x.index("days")
                    index_of_num_day=index_of_day-1
                    time_to_remind=datetime.timedelta(days=int(x[index_of_num_day]))
                    time_to_remind=timenow+time_to_remind
                elif "hour" in x:
                    index_of_day=x.index("hour")
                    index_of_num_day=index_of_day-1
                    time_to_remind=datetime.timedelta(hours=int(x[index_of_num_day]))
                    time_to_remind=timenow+time_to_remind
                elif "hours" in x:
                    index_of_day=x.index("hours")
                    index_of_num_day=index_of_day-1
                    time_to_remind=datetime.timedelta(hours=int(x[index_of_num_day]))
                    time_to_remind=timenow+time_to_remind
                elif "minute" in x:
                    index_of_day=x.index("minute")
                    index_of_num_day=index_of_day-1
                    time_to_remind=datetime.timedelta(minutes=int(x[index_of_num_day]))
                    time_to_remind=timenow+time_to_remind
                elif "minutes" in x:
                    index_of_day=x.index("minutes")
                    index_of_num_day=index_of_day-1
                    time_to_remind=datetime.timedelta(minutes=int(x[index_of_num_day]))
                    time_to_remind=timenow+time_to_remind
                elif "second" in x:
                    index_of_day=x.index("second")
                    index_of_num_day=index_of_day-1
                    time_to_remind=datetime.timedelta(seconds=int(x[index_of_num_day]))
                    time_to_remind=timenow+time_to_remind
                elif "seconds" in x:
                    index_of_day=x.index("seconds")
                    index_of_num_day=index_of_day-1
                    time_to_remind=datetime.timedelta(seconds=int(x[index_of_num_day]))
                    time_to_remind=timenow+time_to_remind
                each_list[2]=time_to_remind
                #convert list to data frame and export 
                record_df=pd.DataFrame(record_list)  
                #print(record_df)
                record_df.to_csv("remind.csv",index=False,header=None)
                
                #show incomplete item
                incomplete_list=[]
                for each_list in record_list:
                    if each_list[3]==0:
                        incomplete_list.append(each_list)
                incomplete_df=pd.DataFrame(incomplete_list)  
                
                print("________________________________________________")
           
                print("INCOMPLETE LIST")
                print(incomplete_df.iloc[:,0])
                
                print("________________________________________________")
                speak.Speak(next_command)
                
                
                
            elif "mark" in x or "complete" in x:
                each_list[3]=1
                #convert list to data frame and export 
                record_df=pd.DataFrame(record_list)  
                record_df.to_csv("remind.csv",index=False,header=None)
                #print(record_df) 
                
                #show incomplete item
                complete_list=[]
                for each_list in record_list:
                    if each_list[3]==1:
                        complete_list.append(each_list)
                complete_df=pd.DataFrame(complete_list)  
                print("________________________________________________")
    
                print("COMPLETE LIST")
                print(complete_df.iloc[:,0])
                
                print("________________________________________________")
                
                speak.Speak(remind_to_speak)
                speak.Speak("is mark as complete")
                
            else:
                pass