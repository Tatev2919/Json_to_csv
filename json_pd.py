#!/usr/bin/env python3

import pandas as pd
import json
import csv

df = pd.read_json('hardening_features.json')
filename = "json_file.csv"
data = []
header = [ "Feature", "Device" , "commands" ]
with open(filename, 'a+', newline='') as file:
    csvwriter = csv.writer(file) 
    csvwriter.writerow(header)
    for index, row in df.itertuples():
        data = []
        data.append(index)
        data.append("\n")
        for key,value in row.items(): 
            data.append(key)
            data.append(value)
        print(data)
        csvwriter.writerow(data)


