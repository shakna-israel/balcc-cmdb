#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import datetime

def prevent_key_errors(dictIn, keyForce):
    """Allow keys that don't exist, but are expected to, to take on default values"""
    dictOut = dictIn
    try:
        dictIn[keyForce]
        if dictIn[keyForce] == None:
            dictOut[keyForce] = "UNKNOWN"
        if dictIn[keyForce] == "":
            dictOut[keyForce] = "UNKNOWN"
    except KeyError:
        dictOut[keyForce] = "UNKNOWN"
    return dictOut

def expand_data(dictIn):
    """Take the data given and make assumptions about it"""
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
        if dictIn[device]['MAC'] != "UNKNOWN":
            if ':' not in dictIn[device]['MAC']:
                dictOut[device]['MAC'] = dictIn[device]['MAC'][:2].upper() + ":" + dictIn[device]['MAC'][2:4].upper() + ":" + dictIn[device]['MAC'][4:6].upper() + ":" + dictIn[device]['MAC'][6:8].upper() + ":" + dictIn[device]['MAC'][8:10].upper() + ":" + dictIn[device]['MAC'][10:12].upper()
        if dictIn[device]['Cost'] != 'UNKNOWN':
            if dictIn[device]['Purchase Date'] != "UNKNOWN":
                purchaseDate = datetime.datetime.strptime(dictIn[device]['Purchase Date'], date_format)
                now = datetime.datetime.now()
                diffTime = now - purchaseDate
                diff = int(diffTime.days/365)
                if diff >= 0 and diff <= 1:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 1.10)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                elif diff >= 1 and diff <= 2:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 1.25)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                elif diff >= 2 and diff <= 3:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 1.5)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                elif diff >= 3 and diff <= 4:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 1.65)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                elif diff >= 4 and diff <= 5:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 1.75)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                elif diff >= 5 and diff <= 6:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 2)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                elif diff >= 6 and diff <= 7:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 2.5)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                elif diff >= 7 and diff <= 8:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 3)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                elif diff >= 8:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 5)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                else:
                    dictOut[device]['Current Worth'] = "UNKNOWN"
    return dictOut

def prevent_default_values(dataFields, dictIn):
    """If the user hasn't supplied a value, make it UNKNOWN"""
    dictOut = dictIn
    for category in dataFields:
        if dictIn[category] == '':
            dictOut[category] = 'UNKNOWN'

def get_data():
    """Load device data from file"""
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
    dataFields = ['SNID', 'Type', 'Model', 'IP', 'MAC', 'Purchase Date', 'Age', 'License', 'Cost', 'Current Worth' 'Operating System', 'Physical Location', 'Phone Type', 'Phone Number', 'Depends On', 'Assigned To', 'Status', 'Expiry Date', 'General Comments']
    fixedDict = {}
    for item in dataFields:
        for device in touchData:
            fixedDict[device] = prevent_key_errors(touchData[device], item)
    touchDate = expand_data(touchData)
    write_data(touchData)
    return dict(touchData)

def write_data(dictIn):
    """Write device data to file"""
    with open(os.path.expanduser("~/.cmdb/data/cmdb.json"), 'w+') as outFile:
        json.dump(dictIn, outFile, sort_keys = True, indent = 4, ensure_ascii = False)

def get_people():
    """Get the registered list of people"""
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
    try:
        touchData['staff'] = list(set(touchData['staff']))
    except KeyError:
        touchData['staff'] = []
    try:
        touchData['students'] = list(set(touchData['students']))
    except KeyError:
        touchData['students'] = []
    try:
        touchData['teachers'] = list(set(touchData['teachers']))
    except KeyError:
        touchData['teachers'] = []
    return dict(touchData)

def remove_person(stringName, role):
    people = get_people()
    students = people['students']
    teachers = people['teachers']
    staff = people['staff']
    if role == 'students':
        students.remove(stringName)
        people['students'] = students
    elif role == 'teachers':
        teachers.remove(stringName)
        people['teachers'] = teachers
    elif role == 'staff':
        staff.remove(stringName)
        people['staff'] = staff
    else:
        return False
    write_people(people)

def write_people(dictIn):
    """Write the list of people to file"""
    with open(os.path.expanduser("~/.cmdb/data/people.json"), 'w+') as outFile:
        json.dump(dictIn, outFile, sort_keys = True, indent = 4, ensure_ascii = False)

def get_location():
    """Get the registered list of locations"""
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
    """Write locations to file"""
    dictOut = {}
    dictOut['locations'] = list(listIn)
    with open(os.path.expanduser("~/.cmdb/data/location.json"), 'w+') as outFile:
        json.dump(dictOut, outFile, sort_keys = True, indent = 4, ensure_ascii = False)

def replace_user_data(originalUser, newUser):
    devices = get_data()
    outDevices = devices
    for device in devices:
        if originalUser == devices[device]['Assigned To']:
            outDevices[device]['Assigned To'] = newUser
    write_data(outDevices)