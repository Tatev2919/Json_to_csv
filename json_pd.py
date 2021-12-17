#!/usr/bin/env python3

import pandas as pd
import json
import csv

df = pd.read_json('hardening_features.json')
#print(df)
#print (colname)
#print(df.dtypes)
filename = "json_file.csv"
data = []
header = [ "Feature", "Device" , "commands" ]
with open(filename, 'a+', newline='') as file:
    csvwriter = csv.writer(file) 
    csvwriter.writerow(header)
    for index, row in df.itertuples():
        #print(row,index)
        data.append(index)
        for key,value in row.items(): 
            #print(key,value)
            data.append(key)
            data.append(value)
            #print("----------------")
        print(data)
        csvwriter.writerow(data)


