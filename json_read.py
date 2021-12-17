#!/usr/bin/env python3

import json
import csv
import os


def reading_json ():
    with open('hardening_features.json', 'r') as openfile:
        data_dict = json.load(openfile)
        data_collecting(data_dict)

def data_collecting(json_object):
    header = ["features", "devices" ]
    devices = []
    data = []
    
    filename = 'json_file.csv'
    if (os.path.exists(filename)) :
        os.remove(filename)

    with open(filename, 'a+', newline='') as file:
        csvwriter = csv.writer(file) 
        csvwriter.writerow(header)
        for key, value in json_object.items() :
            print (key)
            print("-------------")
            for j in json_object[key]:
                devices = []
                data = []
                data.append(j)
                for i in value[j]: 
                    devices.append(i)
                    for m in j[i]:
                        print(m)
                data.append(devices)
                print(devices)
                csvwriter.writerow(data)

reading_json()




