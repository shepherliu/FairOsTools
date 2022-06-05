#!/usr/bin/python3 
# -*- coding: utf-8 -*-
import os
import sys
import json
import mimetypes
import requests
from requests_toolbelt import MultipartEncoder

#create document db
def create_documentDB(pod_name, table_name, si, mutable, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/doc/new'

	data = {
		'pod_name': pod_name,
		'table_name': table_name,
		'si': si,
		'mutable': mutable
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.post(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))

	if res.status_code >= 200 and res.status_code < 300:
		
		ret = {
			'message': 'success',
			'code': res.status_code,
			'data': res.text
		}

		return ret	

	try:
		ret = res.json()
	except:
		ret = {
			'message': res.text,
			'code': 0
		}

	return ret

#list document dbs
def list_documentDBs(pod_name, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/doc/ls?pod_name={0}'.format(pod_name)

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.get(url = host + path, headers = headers, cookies = cookies)

	if res.status_code >= 200 and res.status_code < 300:
		
		ret = {
			'message': 'success',
			'code': res.status_code,
			'data': res.json()
		}

		return ret	

	try:
		ret = res.json()
	except:
		ret = {
			'message': res.text,
			'code': 0
		}

	return ret

#open document db
def open_documentDB(pod_name, table_name, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/doc/open'

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
			'code': res.status_code,
			'data': res.text
		}

		return ret	

	try:
		ret = res.json()

		#already open as also success
		if ret['message'].find('already open') != -1:
			
			ret = {
				'message': 'success',
				'code': 0
			}		
	except:
		ret = {
			'message': res.text,
			'code': 0
		}

	return ret	

#count documents
def count_documents(pod_name, table_name, expr, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/doc/count'

	data = {
		'pod_name': pod_name,
		'table_name': table_name,
		'expr': expr
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.post(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))

	if res.status_code >= 200 and res.status_code < 300:
		
		ret = {
			'message': 'success',
			'code': res.status_code,
			'data': res.text
		}

		return ret	

	try:
		ret = res.json()
	except:
		ret = {
			'message': res.text,
			'code': 0
		}

	return ret

#delete documentDB
def delete_documentDB(pod_name, table_name, cookies = None, host = 'http://localhost:9090'):
	
	path = '/v1/doc/delete'

	data = {
		'pod_name': pod_name,
		'table_name':table_name
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.delete(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))

	if res.status_code >= 200 and res.status_code < 300:
		
		ret = {
			'message': 'success',
			'code': res.status_code,
			'data': res.text
		}

		return ret	

	try:
		ret = res.json()
	except:
		ret = {
			'message': res.text,
			'code': 0
		}

	return ret

#find documents
def find_documents(pod_name, table_name, expr, limit, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/doc/find?pod_name={0}&table_name={1}&expr={2}&limit={3}'.format(pod_name, table_name, expr, limit)

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.get(url = host + path, headers = headers, cookies = cookies)

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': res.status_code,
			'data': res.json()
		}

		return ret	

	try:
		ret = res.json()
	except:
		ret = {
			'message': res.text,
			'code': 0
		}

	return ret

#load json
def load_json(pod_name, table_name, json, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/doc/loadjson'

	basename = os.path.basename(json)

	types, encoding = mimetypes.guess_type(json)

	m = MultipartEncoder(fields = {
		'pod_name': pod_name,
		'table_name': table_name,
		'json': (basename, open(json, 'rb'), types)
	})

	headers = {
		'Content-Type': m.content_type
	}		

	res = requests.post(url = host + path, headers = headers , cookies = cookies, data = m)

	if res.status_code >= 200 and res.status_code < 300:
		
		ret = {
			'message': 'success',
			'code': res.status_code,
			'data': res.text
		}

		return ret	

	try:
		ret = res.json()
	except:
		ret = {
			'message': res.text,
			'code': 0
		}

	return ret		

#index json
def index_json(pod_name, table_name, file, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/doc/indexjson'

	data = {
		'pod_name': pod_name,
		'table_name': table_name,
		'file': file
	}

	headers = {
		'Content-Type': 'application/json'
	}

	res = requests.post(url = host + path, headers = headers , cookies = cookies, data = json.dumps(data))

	if res.status_code >= 200 and res.status_code < 300:
		
		ret = {
			'message': 'success',
			'code': res.status_code,
			'data': res.text
		}

		return ret	

	try:
		ret = res.json()
	except:
		ret = {
			'message': res.text,
			'code': 0
		}

	return ret

#put document
def put_document(pod_name, table_name, doc, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/doc/entry/put'

	data = {
		'pod_name': pod_name,
		'table_name': table_name,
		'doc': doc
	}

	headers = {
		'Content-Type': 'application/json'
	}

	res = requests.post(url = host + path, headers = headers , cookies = cookies, data = json.dumps(data))

	if res.status_code >= 200 and res.status_code < 300:
		
		ret = {
			'message': 'success',
			'code': res.status_code,
			'data': res.text
		}

		return ret	

	try:
		ret = res.json()
	except:
		ret = {
			'message': res.text,
			'code': 0
		}

	return ret

#get document
def get_document(pod_name, table_name, id, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/doc/entry/get?pod_name={0}&table_name={1}&id={2}'.format(pod_name, table_name, id)

	headers = {
		'Content-Type': 'application/json'
	}

	res = requests.get(url = host + path, headers = headers , cookies = cookies)

	if res.status_code >= 200 and res.status_code < 300:
		
		ret = {
			'message': 'success',
			'code': res.status_code,
			'data': res.text
		}

		return ret	

	try:
		ret = res.json()
	except:
		ret = {
			'message': res.text,
			'code': 0
		}

	return ret

#delete docuemnt
def delete_document(pod_name, table_name, id, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/doc/entry/del'

	data = {
		'pod_name': pod_name,
		'table_name': table_name,
		'id': id
	}

	headers = {
		'Content-Type': 'application/json'
	}

	res = requests.delete(url = host + path, headers = headers , cookies = cookies, data = json.dumps(data))

	if res.status_code >= 200 and res.status_code < 300:
		
		ret = {
			'message': 'success',
			'code': res.status_code,
			'data': res.text
		}

		return ret	

	try:
		ret = res.json()
	except:
		ret = {
			'message': res.text,
			'code': 0
		}

	return ret
