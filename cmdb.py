#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template, redirect, request
from processing import get_data, write_data, get_people, get_location

@route('/')
def index():
    data = get_data()
    return template('home',data=data)

@route('/create', method='GET')
def create_get():
    devices = get_data().keys()
    staff = get_people()['staff']
    teachers = get_people()['teachers']
    students = get_people()['students']
    locations = get_location()
    dataFields = ['Router','Switch','Barrix','Software - Individual', 'Software - Subscription','Hub','Desktop Computer','Laptop','Projector','Speakers','Television - CRT', 'Television - LCD', 'Phone']
    return template('generate', dataFields=dataFields, devices=devices, staff=staff, teachers=teachers, students=students, locations=locations)

@route('/create', method='POST')
def create_post():
    deviceType = request.forms.get('type')
    deviceSNID = request.forms.get('snid')
    deviceModel = request.forms.get('model')
    devicePurchaseDate = request.forms.get('purchase-date')
    deviceCost = request.forms.get('cost')
    deviceDependsOn = request.forms.get('depends-on')
    deviceAssignedTo = request.forms.get('assigned-to')
    devicePhysicalLocation = request.forms.get('physical-location')
    deviceStatus = request.forms.get('status')
    try:
        deviceName = deviceSNID + deviceAssignedTo
    except TypeError:
        deviceName = deviceSNID
    devices = get_data()
    devices[deviceName] = {}
    devices[deviceName]['Type'] = deviceType
    devices[deviceName]['SNID'] = deviceSNID
    devices[deviceName]['Model'] = deviceModel
    devices[deviceName]['Purchase Date'] = devicePurchaseDate
    devices[deviceName]['Cost'] = deviceCost
    devices[deviceName]['Depends On'] = deviceDependsOn
    devices[deviceName]['Assigned To'] = deviceAssignedTo
    devices[deviceName]['Physical Location'] = devicePhysicalLocation
    devices[deviceName]['Status'] = deviceStatus
    write_data(devices)
    if 'software' in deviceType.lower():
        redirect('/create/software/' + deviceSNID)
    elif 'desktop' in deviceType.lower():
        redirect('/create/pc/' + deviceSNID)
    elif 'laptop' in deviceType.lower():
        redirect('/create/pc/' + deviceSNID)
    elif 'phone' in deviceType.lower():
        redirect('/create/phone/' + deviceSNID)
    else:
        redirect('/')

@route('/create/<name>/<SNID>', method='GET')
def create_get_more(name,SNID):
    if name == 'phone':
        return template('generate_phone',SNID=SNID)
    elif name == 'pc':
        return template('generate_pc',SNID=SNID)
    elif name == 'software':
        return template('generate_software',SNID=SNID)
    else:
        redirect('/')

@route('/create/<name>', method='POST')
def create_post_more(name):
    devices = get_data()
    deviceSNID = request.forms.get('snid')
    if name == 'phone':
        devicePhone = request.forms.get('phone-number')
        for key in devices.keys():
            for value in devices.values():
                if item['SNID'] == 'deviceSNID':
                    item['Phone Number'] == 'devicePhone'
        write_data(devices)
        redirect('/')
    elif name == 'pc':
        do
    elif name == 'software':
        do
    else:
        redirect('/')

run(host='localhost', port=8080)
