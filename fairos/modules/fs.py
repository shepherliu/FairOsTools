#!/usr/bin/python3 
# -*- coding: utf-8 -*-
import os
import sys
import json
import requests

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

	res = requests.post(url = host + path, headers = headers, cookies = cookies, data = data)

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.text
		}

		return ret

	return res.json()

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

	res = requests.delete(url = host + path, headers = headers, cookies = cookies, data = data)

	if res.status_code >= 200 and res.status_code < 300:

		ret = {
			'message': 'success',
			'code': 0,
			'data': res.text
		}

		return ret

	return res.json()

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
			'code': 0,
			'data': res.json()
		}

		return ret

	return res.json()

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
			'code': 0,
			'data': res.json()
		}

		return ret

	return res.json()

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
			'code': 0,
			'data': res.json()
		}

		return ret

	return res.json()

#upload file
def upload_file(pod_name, pod_dir, filename, block_size = '512', cookies = None, host = 'http://localhost:9090'):

	path = '/v1/file/upload'

	params = {
		'pod_name': pod_name,
		'pod_dir': pod_dir,
		'block_size': block_size
	}

	files = {'files': open(filename,'rb')}

	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'fairOS-dfs-Compression': "gzip"
	}

	res = requests.post(url = host + path, headers = headers , cookies = cookies, params = params, files = files)

	if res.status_code >= 200 and res.status_code < 300:
		
		ret = {
			'message': 'success',
			'code': 0,
			'data': res.json()
		}

		return ret	

	return res.json()		

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

		path = '/v1/file/download'

		res = requests.post(url = host + path, headers = headers, cookies = cookies, data = data)

	if res.status_code >= 200 and res.status_code < 300:
		
		ret = {
			'message': 'success',
			'code': 0,
			'content': res.text
		}

		return ret	

	return res.json()

#share file
def share_file(pod_name, pod_path_file, dest_user, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/file/share'

	data = {
		'pod_name': pod_name,
		'pod_path_file': pod_path_file,
		'dest_user': dest_user
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.post(url = host + path, headers = headers, cookies = cookies, data = data)

	if res.status_code >= 200 and res.status_code < 300:
		
		ret = {
			'message': 'success',
			'code': 0,
			'data': res.json()
		}

		return ret	

	return res.json()

#receive file
def receive_file(pod_name, sharing_ref, dir_path, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/file/receive'

	data = {
		'pod_name': pod_name,
		'sharing_ref': sharing_ref,
		'dir_path': dir_path
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.post(url = host + path, headers = headers, cookies = cookies, data = data)

	if res.status_code >= 200 and res.status_code < 300:
		
		ret = {
			'message': 'success',
			'code': 0,
			'data': res.json()
		}

		return ret	

	return res.json()

#receive file info
def receive_file_info(pod_name, sharing_ref, cookies = None, host = 'http://localhost:9090'):

	path = '/v1/file/receiveinfo'

	data = {
		'pod_name': pod_name,
		'sharing_ref': sharing_ref,
	}

	headers = {
		'Content-Type': 'application/json'
	}	

	res = requests.post(url = host + path, headers = headers, cookies = cookies, data = data)

	if res.status_code >= 200 and res.status_code < 300:
		
		ret = {
			'message': 'success',
			'code': 0,
			'data': res.json()
		}

		return ret	

	return res.json()

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

	res = requests.delete(url = host + path, headers = headers, cookies = cookies, data = data)

	if res.status_code >= 200 and res.status_code < 300:
		
		ret = {
			'message': 'success',
			'code': 0,
			'data': res.text
		}

		return ret	

	return res.json()

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
			'code': 0,
			'data': res.json()
		}

		return ret	

	return res.json()