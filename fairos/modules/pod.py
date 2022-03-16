#!/usr/bin/python3 
# -*- coding: utf-8 -*-
import os
import sys
import json
import requests

#pod receive info
def pod_receiveinfo(reference, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/pod/receiveinfo?reference={0}'.format(reference)

	headers = {
		'Content-Type': 'application/json'
	}

	res = requests.get(url = host + path, headers = headers, cookies = cookies)

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code':0,
			'data': res.json()
		}

		return ret

	return res.json()

#pod receive
def pod_receive(reference, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/pod/receive?reference={0}'.format(reference)

	headers = {
		'Content-Type': 'application/json'
	}

	res = requests.get(url = host + path, headers = headers, cookies = cookies)

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.text
		}

		return ret

	return res.json()			

#new pod
def new_pod(pod_name, password, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/pod/new'

	data = {
		'pod_name': pod_name,
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

	return res.json()

#open pod
def open_pod(pod_name, password, cookies = None, host = 'http://localhost:9090'):	

	path = '/v1/pod/open'

	data = {
		'pod_name': pod_name,
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

	return res.json()

#close pod
def close_pod(pod_name, cookies = None, host = 'http://localhost:9090'):
	
	path = '/v1/pod/close'

	data = {
		'pod_name': pod_name
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

	return res.json()

#sync pod
def sync_pod(pod_name, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/pod/sync'

	data = {
		'pod_name': pod_name
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

	return res.json()

#share pod
def share_pod(pod_name, password, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/pod/share'

	data = {
		'pod_name': pod_name,
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
			'data': res.json()
		}

		return ret

	return res.json()

#delete pod
def delete_pod(pod_name, password, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/pod/delete'

	data = {
		'pod_name': pod_name,
		'password': password
	}

	headers = {
		'Content-Type': 'application/json'
	}

	res = requests.delete(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))	

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code':0,
			'data': res.text
		}

		return ret

	return res.json()	

#list pod
def list_pod(cookies = None, host = 'http://localhost:9090'):

	path = '/v1/pod/ls'

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

#stat pod
def stat_pod(pod_name, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/pod/stat?pod_name={0}'.format(pod_name)

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

#pod present
def pod_present(pod_name, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/pod/present?pod_name={0}'.format(pod_name)

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
