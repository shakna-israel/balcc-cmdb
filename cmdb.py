#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template, redirect, request
from processing import get_data, write_data, get_people, get_location, write_people, write_location, remove_person, replace_user_data, process_table_data, match_results, process_search_table_data
from collections import OrderedDict

@route('/')
def index():
    data = get_data()
    data = OrderedDict(sorted(data.items(), key=lambda t: t[0]))
    return template('home',data=data)

@route('/new/person', method='GET')
def form_person():
    return template('generate_person')

@route('/new/person', method='POST')
def form_person_fetch():
    name = request.forms.get('name')
    role = request.forms.get('role')
    redirect('/add/' + name + '/' + role)

@route('/new/location', method='GET')
def form_location():
    return template('generate_location', POSTURL="/new/location")

@route('/new/location', method='POST')
def form_location_fetch():
    name = request.forms.get('name')
    redirect('/add/location/' + name)

@route('/add/location/<name>')
def add_location(name):
    whileLoop = 0
    while whileLoop == 0:
        name = str(name)
        locations = get_location()
        locations.append(name)
        write_location(locations)
        whileLoop = 1
    redirect('/')

@route('/del/location', method='GET')
def form_del_location():
    Locations = get_location()
    return template('del_location', POSTURL="/del/location", locations=Locations)

@route('/del/location', method='POST')
def form_del_location_fetch():
    name = request.forms.get('name')
    redirect('/del/location/' + str(name))

@route('/del/location/<name>')
def del_location(name):
    whileLoop = 0
    while whileLoop == 0:
        name = str(name)
        if "_" in name:
            name = name.replace("_"," ")
        locations = list(get_location())
        locations.remove(name)
        write_location(locations)
        whileLoop = 1
    redirect('/')


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

@route('/edit/tableData', method='POST')
def get_table_changes():
    tableData = request.forms.get('data')
    process_table_data(tableData)
    redirect('/')

@route('/search/tableData', method='POST')
def get_search_table_changes():
    tableData = request.forms.get('data')
    process_search_table_data(tableData)
    redirect('/')

@route('/query/build', method='POST')
def get_search_submit():
    name = request.forms.get('name')
    if name == "":
        name = False
    snid = request.forms.get('snid')
    if snid == "":
        snid = False
    deviceType = request.forms.get('deviceType')
    if deviceType == "":
        deviceType = False
    model = request.forms.get('model')
    if model == "":
        model = False
    ip = request.forms.get('ip')
    if ip == "":
        ip = False
    mac = request.forms.get('mac')
    if mac == "":
        mac = False
    purchase_date = request.forms.get('purchase_date')
    if purchase_date == "":
        purchase_date = False
    worth = request.forms.get('worth')
    if worth == "":
        worth = False
    age = request.forms.get('age')
    if age == "":
        age = False
    license = request.forms.get('license')
    if license == "":
        license = False
    cost = request.forms.get('cost')
    if cost == "":
        cost = False
    os = request.forms.get('os')
    if os == "":
        os = False
    location = request.forms.get('location')
    if location == "":
        location = False
    phone_type = request.forms.get('phone_type')
    if phone_type == "":
        phone_type = False
    phone_no = request.forms.get('phone_no')
    if phone_no == "":
        phone_no = False
    depend = request.forms.get('depends')
    if depend == "":
        depend = False
    assign = request.forms.get('assign')
    if assign == "":
        assign = False
    status = request.forms.get('status')
    if status == "":
        status = False
    expiry_date = request.forms.get('expiry_date')
    if expiry_date == "":
        expiry_date = False
    comments = request.forms.get('comments')
    if comments == "":
        comments = False
    dictOut = {"name": name, "snid": snid, "type": deviceType, "model": model, "ip": ip, "mac": mac, "purchase_date": purchase_date, "worth": worth, "age": age, "license": license, "cost": cost, "os": os, "location": location, "phone_type": phone_type, "phone_no": phone_no, "depend": depend, "assign": assign, "status": status, "expiry_date": expiry_date, "comments": comments}
    query = "/query?search=True"
    for key, value in dictOut.items():
        if value != False:
            query = query + "&" + key + "=" + value
    redirect(query)

@route('/query')
def search_rest():
    searched = request.query.search
    whileLoop = 0
    while whileLoop == 0:
        name = request.query.name
        if name == "":
            name = False
        snid = request.query.snid
        if snid == "":
            snid = False
        deviceType = request.query.type
        if deviceType == "":
            deviceType = False
        model = request.query.model
        if model == "":
            model = False
        ip = request.query.ip
        if ip == "":
            ip = False
        mac = request.query.mac
        if mac == "":
            mac = False
        purchase_date = request.query.purchase_date
        if purchase_date == "":
            purchase_date = False
        worth = request.query.worth
        if worth == "":
            worth = False
        age = request.query.age
        if age == "":
            age = False
        license = request.query.license
        if license == "":
            license = False
        cost = request.query.cost
        if cost == "":
            cost = False
        os = request.query.os
        if os == "":
            os = False
        location = request.query.location
        if location == "":
            location = False
        phone_type = request.query.phone_type
        if phone_type == "":
            phone_type = False
        phone_no = request.query.phone_no
        if phone_no == "":
            phone_no = False
        depend = request.query.depend
        if depend == "":
            depend = False
        assign = request.query.assign
        if assign == "":
            assign = False
        status = request.query.status
        if status == "":
            status = False
        expiry_date = request.query.expiry_date
        if expiry_date == "":
            expiry_date = False
        comments = request.query.comments
        if comments == "":
            comments = False
        dictOut = {"Name": name, "SNID": snid, "Type": deviceType, "Model": model, "IP": ip, "MAC": mac, "Purchase Date": purchase_date, "Current Worth": worth, "Age": age, "License": license, "Cost": cost, "Operating System": os, "Physical Location": location, "Phone Type": phone_type, "Phone Number": phone_no, "Depends On": depend, "Assigned To": assign, "Status": status, "Expiry Date": expiry_date, "General Comments": comments}
        results = match_results(dictOut, get_data())
        whileLoop = 1
    return template('search', results=results, data=get_data(), searched=searched)

run(host='0.0.0.0', port=8080)
