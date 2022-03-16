#!/usr/bin/python3 
# -*- coding: utf-8 -*-
import os
import sys
import json
import time
import requests

#singup user
def signup_user(user_name, password, host = 'http://localhost:9090' , mnemonic = ''):

	path = '/v1/user/signup';

	headers = {
		'Content-Type': 'application/json'
	}

	data = {
		'user_name': user_name,
		'password': password,
		'mnemonic': mnemonic
	}

	res = requests.post(url = host + path, headers = headers, data = data)

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': {'address':''}
		}

		if mnemonic == '':
			ret['data'] = res.json()

		return ret
	
	return res.json()

#logon user
def login_user(user_name, password, host = 'http://localhost:9090'):
	
	path = '/v1/user/login'

	headers = {
		'Content-Type': 'application/json'
	}

	data = {
		'user_name': user_name,
		'password': password,
	}

	res = requests.post(url = host + path, headers = headers, data = data)

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'cookies': requests.utils.dict_from_cookiejar(res.cookies)
		}

		return ret

	return res.json()

#import user
def import_user(user_name, password, address, host = 'http://localhost:9090'):
	
	path = '/v1/user/import'

	headers = {
		'Content-Type': 'application/json'
	}

	data = {
		'user_name': user_name,
		'password': password,
		'address': address
	}

	res = requests.post(url = host + path, headers = headers, data = data)

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.json(),
			'cookies': requests.utils.dict_from_cookiejar(res.cookies)
		}

		return ret

	return res.json()

#user present
def user_present(user_name, host = 'http://localhost:9090'):

	path = '/v1/user/present?user_name=' + user_name
	
	headers = {
		'Content-Type': 'application/json'
	}

	res = requests.get(url = host + path, headers = headers)

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.json()
		}

		return ret

	return res.json()

#is logged-in
def is_logged_in(user_name, host = 'http://localhost:9090'):
	
	path = '/v1/user/isloggedin?user_name='+user_name

	headers = {
		'Content-Type': 'application/json'
	}

	res = requests.get(url = host + path, headers = headers)

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.json()
		}

		return ret

	return res.json()

#logout user
def user_logout(cookies = None, host = 'http://localhost:9090'):
	
	path = '/v1/user/logout'

	headers = {
		'Content-Type': 'application/json'
	}		

	res = requests.post(url = host + path, headers = headers, cookies = cookies)

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.text
		}

		return ret

	return res.json()

#export user
def export_user(cookies = None, host = 'http://localhost:9090'):
	
	path = '/v1/user/export'

	headers = {
		'Content-Type': 'application/json'
	}		

	res = requests.post(url = host + path, headers = headers, cookies = cookies)

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.json()
		}

		return ret

	return res.json()

#delete user
def delete_user(password, cookies = None, host = 'http://localhost:9090'):
	
	path = '/v1/user/delete'

	data = {
		'password': password
	}

	headers = {
		'Content-Type': 'application/json'
	}		

	res = requests.delete(url = host + path, headers = headers, cookies = cookies, data = data)

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.text
		}

		return ret

	return res.json()	

#user stat
def user_stat(cookies = None, host = 'http://localhost:9090'):
	
	path = '/v1/user/stat'

	headers = {
		'Content-Type': 'application/json'
	}		

	res = requests.get(url = host + path, headers = headers, cookies = cookies)

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.json()
		}

		return ret

	return res.json()			