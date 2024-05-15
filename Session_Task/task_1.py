import pandas 
import csv
from csv import *
import random
from datetime import datetime
import threading 

def runit():
    threading.Timer(10.0, runit).start()
    print("New Data!")
    csvFile = pandas.read_csv('/home/xs450-akatag/Desktop/Session_Task/videos.csv')
    print(csvFile)

    a=100

    while a>0:
        with open('videos.csv','r') as f:
            reader = csv.reader(f)
            chosen_row = random.choice(list(reader))
            print(chosen_row)
        current_date_time = datetime.now() 
        List = [chosen_row, 1, 1, current_date_time]
        
        with open('Videos_Engagement_Metrics.csv', 'a') as f_object:
        
            writer_object = writer(f_object)
        
            writer_object.writerow(List)
        
            # Close the file object
            f_object.close()
            a=a-1

runit()