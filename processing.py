#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import datetime
import math

def match_results(dictIn, dataIn):
    """Match devices against search query data"""
    results = []
    key_list = ["SNID", "Type", "Model", "IP", "MAC", "Purchase Date", "Current Worth", "Age", "License", "Cost", "Operating System", "Physical Location", "Phone Type", "Phone Number", "Depends On", "Assigned To", "Status", "Expiry Date", "General Comments"]
    for device in dataIn:
        for key, value in dictIn.items():
            if value != False:
                if key == "Name":
                    if key in dataIn[device]:
                        results.append(device)
                else:
                    for key_compare in key_list:
                        if key == key_compare:
                            if value in dataIn[device][key_compare]:
                                results.append(device)
    results = list(set(results))
    return results

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

def round_value(inValue):
    return math.ceil(int(inValue)*100/100)

def remove_characters(dictOut, dictIn, device, charList, keyList):
    for key in keyList:
        for item in charList:
            dictOut[device][key] = dictIn[device][key].replace(item,"")
    return dictOut

def expand_data(dictIn):
    """Take the data given and make assumptions about it"""
    dictOut = dictIn
    for device in dictIn:
        # Remove unacceptable characters
        charList = ['"',"'","%","$","|"]
        keyList = ['SNID', 'Type', 'Model', 'IP', 'MAC', 'Purchase Date', 'Age', 'License', 'Cost', 'Current Worth', 'Operating System', 'Physical Location', 'Phone Type', 'Phone Number', 'Depends On', 'Assigned To', 'Status', 'Expiry Date', 'General Comments']
        dictOut = remove_characters(dictOut, dictIn, device, charList, keyList)
        # Calculate the age of the device and insert into Age
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
        # Display MAC Addresses nicely
        if dictIn[device]['MAC'] != "UNKNOWN":
            if ':' not in dictIn[device]['MAC']:
                dictOut[device]['MAC'] = dictIn[device]['MAC'][:2].upper() + ":" + dictIn[device]['MAC'][2:4].upper() + ":" + dictIn[device]['MAC'][4:6].upper() + ":" + dictIn[device]['MAC'][6:8].upper() + ":" + dictIn[device]['MAC'][8:10].upper() + ":" + dictIn[device]['MAC'][10:12].upper()
        # New devices older than one year should become Ok devices.
        if dictIn[device]['Status'] == 'New':
            purchaseDate = datetime.datetime.strptime(dictIn[device]['Purchase Date'], date_format)
            now = datetime.datetime.now()
            diffTime = now - purchaseDate
            diff = int(diffTime.days/365)
            if diff >= 1:
                dictOut[device]['Status'] = 'Ok'
        # Estimate current device worth
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
                        currentWorth = round_value(currentWorth)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                elif diff >= 1 and diff <= 2:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 1.25)
                        currentWorth = round_value(currentWorth)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                elif diff >= 2 and diff <= 3:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 1.5)
                        currentWorth = round_value(currentWorth)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                elif diff >= 3 and diff <= 4:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 1.65)
                        currentWorth = round_value(currentWorth)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                elif diff >= 4 and diff <= 5:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 1.75)
                        currentWorth = round_value(currentWorth)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                elif diff >= 5 and diff <= 6:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 2)
                        currentWorth = round_value(currentWorth)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                elif diff >= 6 and diff <= 7:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 2.5)
                        currentWorth = round_value(currentWorth)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                elif diff >= 7 and diff <= 8:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 4)
                        currentWorth = round_value(currentWorth)
                        dictOut[device]['Current Worth'] = str(currentWorth)
                    except ValueError:
                        dictOut[device]['Current Worth'] = "UNKNOWN"
                elif diff >= 8:
                    try:
                        valueCost = int(dictIn[device]['Cost'])
                        currentWorth = (valueCost / 6)
                        currentWorth = round_value(currentWorth)
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
    dataFields = ['SNID', 'Type', 'Model', 'IP', 'MAC', 'Purchase Date', 'Age', 'License', 'Cost', 'Current Worth', 'Operating System', 'Physical Location', 'Phone Type', 'Phone Number', 'Depends On', 'Assigned To', 'Status', 'Expiry Date', 'General Comments']
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

def backup_data():
    data = get_data()
    with open(os.path.expanduser("~/.cmdb/data/cmdb.json.bak"), 'w+') as outFile:
        json.dump(data, outFile, sort_keys = True, indent = 4, ensure_ascii = False)

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
    dictOut['locations'] = list(set(list(listIn)))
    with open(os.path.expanduser("~/.cmdb/data/location.json"), 'w+') as outFile:
        json.dump(dictOut, outFile, sort_keys = True, indent = 4, ensure_ascii = False)

def replace_user_data(originalUser, newUser):
    devices = get_data()
    outDevices = devices
    for device in devices:
        if originalUser == devices[device]['Assigned To']:
            outDevices[device]['Assigned To'] = newUser
    write_data(outDevices)

def replace_device_data(dictIn):
    os.remove(os.path.expanduser("~/.cmdb/data/cmdb.json"))
    write_data(dictIn)

def process_table_data(longString):
    backup_data()
    dictOut = {}
    longString = longString.replace("$","")
    deviceList = longString.split('%')
    for device in deviceList:
        deviceAttributes = device.split('|')
        if deviceAttributes[0] != '':
            if deviceAttributes[1] != 'REMOVE':
                deviceName = deviceAttributes[0]
                deviceSNID = deviceAttributes[1]
                deviceType = deviceAttributes[2]
                deviceModel = deviceAttributes[3]
                deviceIP = deviceAttributes[4]
                deviceMAC = deviceAttributes[5]
                devicePurchaseDate = deviceAttributes[6]
                deviceLicense = deviceAttributes[7]
                deviceCost = deviceAttributes[8]
                deviceOS = deviceAttributes[9]
                deviceLocation = deviceAttributes[10]
                devicePhoneType = deviceAttributes[11]
                devicePhoneNumber = deviceAttributes[12]
                deviceDependsOn = deviceAttributes[13]
                deviceAssignedTo = deviceAttributes[14]
                deviceStatus = deviceAttributes[15]
                deviceExpiryDate = deviceAttributes[16]
                deviceGeneralComments = deviceAttributes[17]
                dictOut[deviceName] = {}
                dictOut[deviceName]['SNID'] = deviceSNID
                dictOut[deviceName]['Type'] = deviceType
                dictOut[deviceName]['Model'] = deviceModel
                dictOut[deviceName]['IP'] = deviceIP
                dictOut[deviceName]['MAC'] = deviceMAC
                dictOut[deviceName]['Purchase Date'] = devicePurchaseDate
                dictOut[deviceName]['License'] = deviceLicense
                dictOut[deviceName]['Cost'] = deviceCost
                dictOut[deviceName]['Operating System'] = deviceOS
                dictOut[deviceName]['Physical Location'] = deviceLocation
                dictOut[deviceName]['Phone Type'] = devicePhoneType
                dictOut[deviceName]['Phone Number'] = devicePhoneNumber
                dictOut[deviceName]['Depends On'] = deviceDependsOn
                dictOut[deviceName]['Assigned To'] = deviceAssignedTo
                dictOut[deviceName]['Status'] = deviceStatus
                dictOut[deviceName]['Expiry Date'] = deviceExpiryDate
                dictOut[deviceName]['General Comments'] = deviceGeneralComments
    replace_device_data(dictOut)

def process_search_table_data(longString):
    backup_data()
    data = get_data()
    longString = longString.replace("$","")
    deviceList = longString.split('%')
    for device in deviceList:
        deviceAttributes = device.split('|')
        if deviceAttributes[0] != '':
            if deviceAttributes[1] != 'REMOVE':
                deviceName = deviceAttributes[0]
                deviceSNID = deviceAttributes[1]
                deviceType = deviceAttributes[2]
                deviceModel = deviceAttributes[3]
                deviceIP = deviceAttributes[4]
                deviceMAC = deviceAttributes[5]
                devicePurchaseDate = deviceAttributes[6]
                deviceLicense = deviceAttributes[7]
                deviceCost = deviceAttributes[8]
                deviceOS = deviceAttributes[9]
                deviceLocation = deviceAttributes[10]
                devicePhoneType = deviceAttributes[11]
                devicePhoneNumber = deviceAttributes[12]
                deviceDependsOn = deviceAttributes[13]
                deviceAssignedTo = deviceAttributes[14]
                deviceStatus = deviceAttributes[15]
                deviceExpiryDate = deviceAttributes[16]
                deviceGeneralComments = deviceAttributes[17]
                data[deviceName] = {}
                data[deviceName]['SNID'] = deviceSNID
                data[deviceName]['Type'] = deviceType
                data[deviceName]['Model'] = deviceModel
                data[deviceName]['IP'] = deviceIP
                data[deviceName]['MAC'] = deviceMAC
                data[deviceName]['Purchase Date'] = devicePurchaseDate
                data[deviceName]['License'] = deviceLicense
                data[deviceName]['Cost'] = deviceCost
                data[deviceName]['Operating System'] = deviceOS
                data[deviceName]['Physical Location'] = deviceLocation
                data[deviceName]['Phone Type'] = devicePhoneType
                data[deviceName]['Phone Number'] = devicePhoneNumber
                data[deviceName]['Depends On'] = deviceDependsOn
                data[deviceName]['Assigned To'] = deviceAssignedTo
                data[deviceName]['Status'] = deviceStatus
                data[deviceName]['Expiry Date'] = deviceExpiryDate
                data[deviceName]['General Comments'] = deviceGeneralComments
    replace_device_data(data)