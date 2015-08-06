#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template
from processing import get_data, write_data

@route('/')
def index():
    data = get_data()
    return template('home',data=data)

@route('/create')
def create_get():
	return template('generate')

run(host='localhost', port=8080)
