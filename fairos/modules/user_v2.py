#!/usr/bin/python3 
# -*- coding: utf-8 -*-
import os
import sys
import json
import time
import requests

#singup user
def signup_user(user_name, password, host = 'http://localhost:9090' , mnemonic = ''):

	path = '/v2/user/signup';

	headers = {
		'Content-Type': 'application/json'
	}

	data = {
		'user_name': user_name,
		'password': password,
		'mnemonic': mnemonic
	}

	res = requests.post(url = host + path, headers = headers, data = json.dumps(data))

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': {'address':''}
		}

		# if mnemonic == '':
		ret['data'] = res.json()

		return ret
	
	try:
		ret = res.json()
	except:
		ret = {
			'message': ret.text(),
			'code': 0
		}

	return ret

#logon user
def login_user(user_name, password, host = 'http://localhost:9090'):
	
	path = '/v2/user/login'

	headers = {
		'Content-Type': 'application/json'
	}

	data = {
		'user_name': user_name,
		'password': password,
	}

	res = requests.post(url = host + path, headers = headers, data = json.dumps(data))

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'cookies': requests.utils.dict_from_cookiejar(res.cookies),
			'data': res.json()
		}

		return ret

	try:
		ret = res.json()
	except:
		ret = {
			'message': ret.text(),
			'code': 0
		}

	return ret

#import user
# def import_user(user_name, password, address, host = 'http://localhost:9090'):
	
# 	path = '/v2/user/import'

# 	headers = {
# 		'Content-Type': 'application/json'
# 	}

# 	data = {
# 		'user_name': user_name,
# 		'password': password,
# 		'address': address
# 	}

# 	res = requests.post(url = host + path, headers = headers, data = json.dumps(data))

# 	if res.status_code >= 200 and res.status_code < 300:

# 		ret = {
# 			'message': 'success',
# 			'code': 0,
# 			'data': res.json(),
# 			'cookies': requests.utils.dict_from_cookiejar(res.cookies)
# 		}

# 		return ret

# 	try:
# 		ret = res.json()
# 	except:
# 		ret = {
# 			'message': ret.text(),
# 			'code': 0
# 		}

# 	return ret

#user present
def user_present(user_name, host = 'http://localhost:9090'):

	path = '/v2/user/present?user_name=' + user_name
	
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

	try:
		ret = res.json()
	except:
		ret = {
			'message': ret.text(),
			'code': 0
		}

	return ret

#is logged-in
# def is_logged_in(user_name, host = 'http://localhost:9090'):
	
# 	path = '/v2/user/isloggedin?user_name='+user_name

# 	headers = {
# 		'Content-Type': 'application/json'
# 	}

# 	res = requests.get(url = host + path, headers = headers)

# 	if res.status_code >= 200 and res.status_code < 300:

# 		ret = {
# 			'message': 'success',
# 			'code': 0,
# 			'data': res.json()
# 		}

# 		return ret

# 	try:
# 		ret = res.json()
# 	except:
# 		ret = {
# 			'message': ret.text(),
# 			'code': 0
# 		}

# 	return ret

#logout user
# def user_logout(cookies = None, host = 'http://localhost:9090'):
	
# 	path = '/v2/user/logout'

# 	headers = {
# 		'Content-Type': 'application/json'
# 	}		

# 	res = requests.post(url = host + path, headers = headers, cookies = cookies)

# 	if res.status_code >= 200 and res.status_code < 300:

# 		ret = {
# 			'message': 'success',
# 			'code': 0,
# 			'data': res.text
# 		}

# 		return ret

# 	try:
# 		ret = res.json()
# 	except:
# 		ret = {
# 			'message': ret.text(),
# 			'code': 0
# 		}

# 	return ret

#export user
# def export_user(cookies = None, host = 'http://localhost:9090'):
	
# 	path = '/v2/user/export'

# 	headers = {
# 		'Content-Type': 'application/json'
# 	}		

# 	res = requests.post(url = host + path, headers = headers, cookies = cookies)

# 	if res.status_code >= 200 and res.status_code < 300:

# 		ret = {
# 			'message': 'success',
# 			'code': 0,
# 			'data': res.json()
# 		}

# 		return ret

# 	try:
# 		ret = res.json()
# 	except:
# 		ret = {
# 			'message': ret.text(),
# 			'code': 0
# 		}

# 	return ret

#migrate user
def migrate_user(password, cookies = None, host = 'http://localhost:9090'):

	path = '/v2/user/migrate'

	data = {
		'password': password
	}

	headers = {
		'Content-Type': 'application/json'
	}		

	res = requests.post(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.text
		}

		return ret

	try:
		ret = res.json()
	except:
		ret = {
			'message': ret.text(),
			'code': 0
		}

	return ret	

#delete user
def delete_user(password, cookies = None, host = 'http://localhost:9090'):
	
	path = '/v2/user/delete'

	data = {
		'password': password
	}

	headers = {
		'Content-Type': 'application/json'
	}		

	res = requests.delete(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.text
		}

		return ret

	try:
		ret = res.json()
	except:
		ret = {
			'message': ret.text(),
			'code': 0
		}

	return ret

#user stat
# def user_stat(cookies = None, host = 'http://localhost:9090'):
	
# 	path = '/v2/user/stat'

# 	headers = {
# 		'Content-Type': 'application/json'
# 	}		

# 	res = requests.get(url = host + path, headers = headers, cookies = cookies)

# 	if res.status_code >= 200 and res.status_code < 300:

# 		ret = {
# 			'message': 'success',
# 			'code': 0,
# 			'data': res.json()
# 		}

# 		return ret

# 	try:
# 		ret = res.json()
# 	except:
# 		ret = {
# 			'message': ret.text(),
# 			'code': 0
# 		}

# 	return ret		