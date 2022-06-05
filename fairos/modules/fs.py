#!/usr/bin/python3 
# -*- coding: utf-8 -*-
import os
import sys
import json
import mimetypes
import requests
from requests_toolbelt import MultipartEncoder

#make dir
def make_dir(pod_name, dir_path, cookies = None, host = 'http://localhost:9090'):
	
	path = '/v1/dir/mkdir'

	data = {
		'pod_name': pod_name,
		'dir_path': dir_path
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

#remove dir
def remove_dir(pod_name, dir_path, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/dir/rmdir'

	data = {
		'pod_name': pod_name,
		'dir_path': dir_path
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

#list dir
def list_dir(pod_name, dir_path, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/dir/ls?pod_name={0}&dir_path={1}'.format(pod_name, dir_path)

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

#stat dir
def stat_dir(pod_name, dir_path, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/dir/stat?pod_name={0}&dir_path={1}'.format(pod_name, dir_path)

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

#dir present
def dir_present(pod_name, dir_path, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/dir/present?pod_name={0}&dir_path={1}'.format(pod_name, dir_path)

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

#upload file
def upload_file(pod_name, dir_path, filename, block_size = '512', cookies = None, host = 'http://localhost:9090'):

	path = '/v1/file/upload'

	basename = os.path.basename(filename)

	types, encoding = mimetypes.guess_type(filename)

	m = MultipartEncoder(fields = {
		'pod_name': pod_name,
		'dir_path': dir_path,
		'block_size': block_size,
		'files': (basename, open(filename, 'rb'), types)
	})

	headers = {
		'Content-Type': m.content_type,
		'fairOS-dfs-Compression': "gzip"
	}

	res = requests.post(url = host + path, headers = headers , cookies = cookies, data = m)

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

#download file
def download_file(pod_name, file_path, request_type = 'post', cookies = None, host = 'http://localhost:9090'):

	headers = {
		'Content-Type': 'application/json'
	}	

	data = {
		'pod_name': pod_name,
		'file_path': file_path
	}	

	if request_type == 'get':
		
		path = '/v1/file/download?pod_name={0}&file_path={1}'.format(pod_name, file_path)

		res = requests.get(url = host + path, headers = headers, cookies = cookies)
	else:

		path = '/v1/file/download?pod_name={0}&file_path={1}'.format(pod_name, file_path)

		res = requests.post(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))

	help(res)

	if res.status_code >= 200 and res.status_code < 300:
		
		ret = {
			'message': 'success',
			'code': res.status_code,
			'content': res.text
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

#share file
def share_file(pod_name, file_path, dest_user, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/file/share'

	data = {
		'pod_name': pod_name,
		'file_path': file_path,
		'dest_user': dest_user
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.post(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))

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

#receive file
def receive_file(pod_name, sharing_ref, dir_path, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/file/receive?pod_name={0}&sharing_ref={1}&dir_path={2}'.format(pod_name,sharing_ref,dir_path)

	data = {
		'pod_name': pod_name,
		'sharing_ref': sharing_ref,
		'dir_path': dir_path
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.get(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))

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

#receive file info
def receive_file_info(pod_name, sharing_ref, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/file/receiveinfo?pod_name={0}&sharing_ref={1}'.format(pod_name,sharing_ref)

	data = {
		'pod_name': pod_name,
		'sharing_ref': sharing_ref,
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.get(url = host + path, headers = headers, cookies = cookies, data = json.dumps(data))

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

#delete info
def delete_info(pod_name, file_path, cookies = None, host = 'http://localhost:9090'):
	
	path = '/v1/file/delete'

	data = {
		'pod_name': pod_name,
		'file_path': file_path,
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

#stat info
def stat_info(pod_name, file_path, cookies = None, host = 'http://localhost:9090'):
	
	path = '/v1/file/stat?pod_name={0}&file_path={1}'.format(pod_name, file_path)

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
