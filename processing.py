#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import datetime

def prevent_key_errors(dictIn, keyForce):
    dictOut = dictIn
    try:
        dictIn[keyForce]
        if dictIn[keyForce] == None:
            dictOut[keyForce] = "UNKNOWN"
    except KeyError:
        dictOut[keyForce] = "UNKNOWN"
    return dictOut

def expand_data(dictIn):
    dictOut = dictIn
    for device in dictIn:
        try:
            date_format = "%d/%m/%Y"
            purchaseDate = datetime.datetime.strptime(dictIn[device]['Purchase Date'], date_format)
            now = datetime.datetime.now()
            diff = now - purchaseDate
            dictOut[device]['Age'] = str(diff.days/365) + " years."
        except ValueError:
            dictOut[device]['Age'] = "UNKNOWN"
        except TypeError:
            dictOut[device]['Age'] = "UNKNOWN"
    return dictOut

def prevent_default_values(dataFields, dictIn):
    dictOut = dictIn
    for category in dataFields:
        if dictIn[category] == '':
            dictOut[category] = 'UNKNOWN'

def get_data():
    if not os.path.isdir(os.path.expanduser("~/.cmdb/data")):
        if not os.path.isdir(os.path.expanduser("~/.cmdb")):
            os.mkdir(os.path.expanduser("~/.cmdb"))
            os.mkdir(os.path.expanduser("~/.cmdb/data"))
        else:
            os.mkdir(os.path.expanduser("~/.cmdb/data"))
    if not os.path.isfile(os.path.expanduser("~/.cmdb/data/cmdb.json")):
        touchData = {}
        write_data(touchData)
    else:
        with open(os.path.expanduser("~/.cmdb/data/cmdb.json"),'r') as inFile:
            touchData = json.load(inFile)
    dataFields = ['SNID', 'Type', 'Model', 'IP', 'MAC', 'Purchase Date', 'Age', 'License', 'Cost', 'Operating System', 'Physical Location', 'Phone Type', 'Phone Number', 'Depends On', 'Assigned To', 'Status', 'Expiry Date', 'General Comments']
    fixedDict = {}
    for item in dataFields:
        for device in touchData:
            fixedDict[device] = prevent_key_errors(touchData[device], item)
    touchDate = expand_data(touchData)
    write_data(touchData)
    return dict(touchData)

def write_data(dictIn):
    with open(os.path.expanduser("~/.cmdb/data/cmdb.json"), 'w+') as outFile:
        json.dump(dictIn, outFile, sort_keys = True, indent = 4, ensure_ascii = False)

def get_people():
    if not os.path.isdir(os.path.expanduser("~/.cmdb/data")):
        if not os.path.isdir(os.path.expanduser("~/.cmdb")):
            os.mkdir(os.path.expanduser("~/.cmdb"))
            os.mkdir(os.path.expanduser("~/.cmdb/data"))
        else:
            os.mkdir(os.path.expanduser("~/.cmdb/data"))
    if not os.path.isfile(os.path.expanduser("~/.cmdb/data/people.json")):
        touchData = {}
        write_people(touchData)
    else:
        with open(os.path.expanduser("~/.cmdb/data/people.json"),'r') as inFile:
            touchData = json.load(inFile)
    return dict(touchData)

def write_people(dictIn):
    with open(os.path.expanduser("~/.cmdb/data/people.json"), 'w+') as outFile:
        json.dump(dictIn, outFile, sort_keys = True, indent = 4, ensure_ascii = False)

def get_location():
    if not os.path.isdir(os.path.expanduser("~/.cmdb/data")):
        if not os.path.isdir(os.path.expanduser("~/.cmdb")):
            os.mkdir(os.path.expanduser("~/.cmdb"))
            os.mkdir(os.path.expanduser("~/.cmdb/data"))
        else:
            os.mkdir(os.path.expanduser("~/.cmdb/data"))
    if not os.path.isfile(os.path.expanduser("~/.cmdb/data/location.json")):
        touchData = {}
        touchData['locations'] = []
        write_location(touchData)
    else:
        with open(os.path.expanduser("~/.cmdb/data/location.json"),'r') as inFile:
            touchData = json.load(inFile)
    return list(touchData['locations'])

def write_location(listIn):
    dictOut = {}
    dictOut['locations'] = list(listIn)
    with open(os.path.expanduser("~/.cmdb/data/location.json"), 'w+') as outFile:
        json.dump(dictOut, outFile, sort_keys = True, indent = 4, ensure_ascii = False)