#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template, redirect, request
from processing import get_data, write_data, get_people, get_location, write_people, remove_person, replace_user_data

@route('/')
def index():
    data = get_data()
    return template('home',data=data)

@route('/new/person', method='GET')
def form_person():
    return template('generate_person')

@route('/new/person', method='POST')
def form_person_fetch():
    name = request.forms.get('name')
    role = request.forms.get('role')
    redirect('/add/' + name + '/' + role)

@route('/add/<name>/<role>')
def add_person(name, role):
    if role == 'students':
        people = get_people()
        people['students'].append(name)
        write_people(people)
        redirect('/added/' + name + '/' + role)
    elif role == 'teachers':
        people = get_people()
        people['teachers'].append(name)
        write_people(people)
        redirect('/added/' + name + '/' + role)
    elif role == 'staff':
        people = get_people()
        people['staff'].append(name)
        write_people(people)
        redirect('/added/' + name + '/' + role)
    else:
        redirect('/')

@route('/edit/person', method='GET')
def form_edit_person():
    people = get_people()
    teachers = people['teachers']
    staff = people['staff']
    students = people['students']
    return template('edit_person',teachers=teachers,staff=staff,students=students)

@route('/edit/person', method='POST')
def form_edit_person_submitted():
    submission = request.forms.get('name')
    submission = submission.split(':')
    userRole = submission[0]
    userName = submission[1]
    originalUserName = submission[1]
    remove_person(userName, userRole)
    if request.forms.get('new_name'):
        userName = request.forms.get('new_name')
    if request.forms.get('new_role'):
        userRole = request.forms.get('new_role')

    replace_user_data(originalUserName, userName)

    redirect('/add/' + userName + '/' + userRole)

@route('/added/<person>/<role>')
def added_person(person, role):
    return template('wrote_person',person=person,role=role)

@route('/del/person', method='GET')
def form_delete_person():
    people = get_people()
    teachers = people['teachers']
    staff = people['staff']
    students = people['students']
    return template('remove_person',teachers=teachers,staff=staff,students=students)

@route('/del/person', method='POST')
def form_delete_person_submitted():
    submission = request.forms.get('name')
    submission = submission.split(':')
    userRole = submission[0]
    userName = submission[1]
    remove_person(userName, userRole)
    redirect('/')

@route('/create', method='GET')
def create_get():
    devices = get_data().keys()
    staff = get_people()['staff']
    teachers = get_people()['teachers']
    students = get_people()['students']
    locations = get_location()
    print(locations)
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
        for value in devices.values():
            if value['SNID'] == deviceSNID:
                value['Phone Number'] == 'devicePhone'
        write_data(devices)
        redirect('/')
    elif name == 'pc':
        deviceIP = request.forms.get('ip_address')
        deviceMAC = request.forms.get('mac_address')
        deviceOS = request.forms.get('operating_system')
        for value in devices.values():
            if value['SNID'] == deviceSNID:
                value['IP'] = deviceIP
                value['MAC'] = deviceMAC
                value['Operating System'] = deviceOS
        write_data(devices)
        redirect('/')
    elif name == 'software':
        deviceLicense = request.forms.get('license')
        deviceExpiry = request.forms.get('expiry_date')
        for value in devices.values():
            if value['SNID'] == deviceSNID:
                value['License'] = deviceLicense
                value['Expiry Date'] = deviceExpiry
        write_data(devices)
        redirect('/')
    else:
        redirect('/')

run(host='0.0.0.0', port=8080)
