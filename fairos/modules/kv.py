#!/usr/bin/python3 
# -*- coding: utf-8 -*-
import os
import sys
import json
import requests

#create new table
def create_new_table(pod_name, table_name, indexType, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/kv/new'

	data = {
		'pod_name': pod_name,
		'table_name': table_name,
		'indexType': indexType
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.post(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))	

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.text,
		}

		return ret

	return res.json()

#list tables
def list_tables(pod_name, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/kv/ls?pod_name={0}'.format(pod_name)

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.get(url = host + path, headers = headers, cookies = cookies)	

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.json(),
		}

		return ret

	return res.json()

#open table
def open_table(pod_name, table_name, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/kv/open'

	data = {
		'pod_name': pod_name,
		'table_name': table_name
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.post(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))	

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.text,
		}

		return ret

	return res.json()

#count table
def count_table(pod_name, table_name, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/kv/count'

	data = {
		'pod_name': pod_name,
		'table_name': table_name
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.post(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))	

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.json(),
		}

		return ret

	return res.json()

#delete table
def delete_table(pod_name, table_name, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/kv/delete'

	data = {
		'pod_name': pod_name,
		'table_name': table_name
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.delete(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))	

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.text,
		}

		return ret

	return res.json()

#put key value
def put_key_value(pod_name, table_name, key, value, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/kv/entry/put'

	data = {
		'pod_name': pod_name,
		'table_name': table_name,
		'key': key,
		'value': value
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.post(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))	

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.text,
		}

		return ret

	return res.json()

#get value
def get_value(pod_name, table_name, key, format = '', cookies = None, host = 'http://localhost:9090'):

	if format == '':

		path = '/v1/kv/entry/get?pod_name={0}&table_name={1}&key={2}'.format(pod_name, table_name, key)

	else:		

		path = '/v1/kv/entry/get-data?pod_name={0}&table_name={1}&key={2}&format={3}'.format(pod_name, table_name, key, format)

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.get(url = host + path, headers = headers, cookies = cookies)	

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.json(),
		}

		return ret

	return res.json()

#delete value
def delete_value(pod_name, table_name, key, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/kv/entry/del'

	data = {
		'pod_name': pod_name,
		'table_name': table_name,
		'key': key
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.post(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))	

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.text,
		}

		return ret

	return res.json()

#seek key
def seek_key(pod_name, table_name, start, end, limit, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/kv/seek'

	data = {
		'pod_name': pod_name,
		'table_name': table_name,
		'start': start,
		'end': end,
		'limit': limit
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.post(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))	

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.text,
		}

		return ret

	return res.json()

#get next
def get_next(pod_name, table_name, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/kv/seek/next?table_name={0}&table_name={1}'.format(pod_name, table_name)

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.get(url = host + path, headers = headers, cookies = cookies)	

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.json(),
		}

		return ret

	return res.json()

#load csv
def load_csv(pod_name, table_name, memory, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/kv/loadcsv'

	data = {
		'pod_name': pod_name,
		'table_name': table_name,
		'memory': memory
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.post(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))	

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.text,
		}

		return ret

	return res.json()

#key present
def key_present(pod_name, table_name, key, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/kv/present?pod_name={0}&table_name={1}&key={2}'.format(pod_name, table_name, key)

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.get(url = host + path, headers = headers, cookies = cookies)	

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.json(),
		}

		return ret

	return res.json()	
