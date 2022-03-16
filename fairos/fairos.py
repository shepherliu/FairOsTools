#!/usr/bin/python3 
# -*- coding: utf-8 -*-
import os
import sys
import json
import requests

import modules

class Fairos(object):
	"""docstring for Fairos"""
	def __init__(self, host = 'http://localhost:9090'):
		super(Fairos, self).__init__()
		self.__host = host
		self.__cookies = None
		self.__user_name = ''
		self.__password = ''

	"""
		fairos api response struct
		{
			'message': 'success', 
			'code': 0,
			'cookies': object
			'data': json or text
		}

		message return success or other error message
		code retun error code
		cookies return fairos cookies
		data return fairos data, detail see: https://docs.modules.fairdatasociety.org/api/
	"""

	"""user functions"""

	#https://docs.modules.fairdatasociety.org/api/#tag/User/paths/~1user~1signup/post
	def signup_user(user_name:str, password:str, mnemonic = ''):

		return modules.signup_user(user_name, password, mnemonic = mnemonic, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/User/paths/~1user~1login/post
	def login_user(user_name:str, password:str):

		res = modules.login_user(user_name, password, host = self.__host)

		if res['message'] == 'success':
			self.__user_name = user_name
			self.__password = password
			self.__cookies = res['cookies']

		return res

	#https://docs.modules.fairdatasociety.org/api/#tag/User/paths/~1user~1import/post
	def import_user(user_name:str, password:str, address:str):

		res = modules.import_user(user_name, password, address, host = self.__host)

		if res['message'] == 'success':
			self.__user_name = user_name
			self.__password = password
			self.__cookies = res['cookies']

		return res

	#https://docs.modules.fairdatasociety.org/api/#tag/User/paths/~1user~1present/get
	def user_present(user_name:str):

		return modules.user_present(user_name, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/User/paths/~1user~1isloggedin/get
	def is_logged_in(user_name:str):
		
		return modules.is_logged_in(user_name, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/User/paths/~1user~1logout/post
	def user_logout():

		res = modules.user_logout(cookies = self.__cookies, host = self.__host)	

		self.__cookies = None
		self.__user_name = ''
		self.__password = ''

		return res

	#https://docs.modules.fairdatasociety.org/api/#tag/User/paths/~1user~1export/post
	def export_user():

		return modules.export_user(cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/User/paths/~1user~1delete/delete
	def delete_user(password:str):

		res = modules.delete_user(password, cookies = self.__cookies, host = self.__host)

		self.__cookies = None
		self.__user_name = ''
		self.__password = ''

		return res

	#https://docs.modules.fairdatasociety.org/api/#tag/User/paths/~1user~1stat/get
	def user_stat():

		return modules.user_stat(cookies = self.__cookies, host = self.__host)

	"""pod functions """

	#https://docs.modules.fairdatasociety.org/api/#tag/Pod/paths/~1pod~1receiveinfo/get
	def pod_receiveinfo(reference:str):

		return modules.pod_receiveinfo(reference, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Pod/paths/~1pod~1receive/get
	def pod_receive(reference:str):

		return modules.pod_receive(reference, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Pod/paths/~1pod~1new/post
	def new_pod(pod_name:str):

		res = modules.new_pod(pod_name, self.__password, cookies = self.__cookies, host = self.__host)

		if res['message'] == 'success':
			self.__cookies = res['cookies']

		return res

	#https://docs.modules.fairdatasociety.org/api/#tag/Pod/paths/~1pod~1open/post
	def open_pod(pod_name:str):

		res = modules.open_pod(pod_name, self.__password, cookies = self.__cookies, host = self.__host)

		if res['message'] == 'success':
			self.__cookies = res['cookies']

		return res

	#https://docs.modules.fairdatasociety.org/api/#tag/Pod/paths/~1pod~1close/post
	def close_pod(pod_name:str):

		return modules.close_pod(pod_name, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Pod/paths/~1pod~1sync/post
	def sync_pod(pod_name:str):

		return modules.sync_pod(pod_name, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Pod/paths/~1pod~1share/post
	def share_pod(pod_name:str):

		return modules.share_pod(pod_name, self.__password, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Pod/paths/~1pod~1delete/delete
	def delete_pod(pod_name:str):

		return modules.delete_pod(pod_name, self.__password, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Pod/paths/~1pod~1ls/get
	def list_pod():

		return modules.list_pod(cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Pod/paths/~1pod~1stat/get
	def stat_pod(pod_name:str):

		return modules.stat_pod(pod_name, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Pod/paths/~1pod~1present/get
	def pod_present(pod_name:str):

		return modules.pod_present(pod_name, cookies = self.__cookies, host = self.__host)

	"""filesystem functions"""

	#https://docs.modules.fairdatasociety.org/api/#tag/File-System/paths/~1dir~1mkdir/post
	def make_dir(pod_name:str, dir_path:str):

		return modules.make_dir(pod_name, dir_path, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/File-System/paths/~1dir~1rmdir/delete
	def remove_dir(pod_name:str, dir_path:str):

		return modules.remove_dir(pod_name, dir_path, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/File-System/paths/~1dir~1ls/get
	def list_dir(pod_name:str, dir_path:str):

		return modules.list_dir(pod_name, dir_path, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/File-System/paths/~1dir~1stat/get
	def stat_dir(pod_name:str, dir_path:str):

		return modules.stat_dir(pod_name, dir_path, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/File-System/paths/~1dir~1present/get
	def dir_present(pod_name:str, dir_path:str):

		return modules.dir_present(pod_name, dir_path, cookies = self.__cookies, host =self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/File-System/paths/~1file~1upload/post
	def upload_file(pod_name:str, pod_dir:str, filename:str, block_size = '512'):

		return modules.upload_file(pod_name, pod_dir, filename, block_size = block_size, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/File-System/paths/~1file~1download/get
	def download_file(pod_name:str, file_path:str, request_type = 'post'):

		return modules.download_file(pod_name, file_path, request_type = request_type, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/File-System/paths/~1file~1share/post
	def share_file(pod_name:str, pod_path_file:str, dest_user:str):

		return modules.share_file(pod_name, pod_path_file, dest_user, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/File-System/paths/~1file~1receive/get
	def receive_file(pod_name:str, sharing_ref:str, dir_path:str):

		return modules.receive_file(pod_name, sharing_ref, dir_path, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/File-System/paths/~1file~1receiveinfo/get
	def receive_file_info(pod_name:str, sharing_ref:str):

		return modules.receive_file_info(pod_name, sharing_ref, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/File-System/paths/~1file~1delete/delete
	def delete_info(pod_name:str, file_path:str):

		return modules.delete_info(pod_name, file_path, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/File-System/paths/~1file~1stat/get
	def stat_info(pod_name:str, file_path:str):

		return modules.stat_info(pod_name, file_path, cookies = self.__cookies, host = self.__host)

	"""kv functions """

	#https://docs.modules.fairdatasociety.org/api/#tag/Key-Value-Store/paths/~1kv~1new/post
	#indexType = 'string' or 'number'
	def create_new_table(pod_name:str, table_name:str, indexType = 'string'):

		return modules.create_new_table(pod_name, table_name, indexType, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Key-Value-Store/paths/~1kv~1ls/get
	def list_tables(pod_name:str):

		return modules.list_tables(pod_name, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Key-Value-Store/paths/~1kv~1open/post
	def open_table(pod_name:str, table_name:str):

		return modules.open_table(pod_name, table_name, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Key-Value-Store/paths/~1kv~1count/post
	def count_table(pod_name:str, table_name:str):

		return modules.count_table(pod_name, table_name, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Key-Value-Store/paths/~1kv~1delete/delete
	def delete_table(pod_name:str, table_name:str):

		return modules.delete_table(pod_name, table_name, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Key-Value-Store/paths/~1kv~1entry~1put/post
	def put_key_value(pod_name:str, table_name:str, key:str, value:str):

		return modules.put_key_value(pod_name, table_name, key, value, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Key-Value-Store/paths/~1kv~1entry~1get/get
	#format = '' or 'string' or 'byte-string'
	def get_value(pod_name:str, table_name:str, key:str, format = ''):

		return modules.get_value(pod_name, table_name, key, format = format, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Key-Value-Store/paths/~1kv~1entry~1del/delete
	def delete_value(pod_name:str, table_name:str, key:str):

		return modules.delete_value(pod_name, table_name, key, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Key-Value-Store/paths/~1kv~1seek/post
	def seek_key(pod_name:str, table_name:str, start:str, end:str, limit:int):

		return modules.seek_key(pod_name, table_name, start, end, limit, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Key-Value-Store/paths/~1kv~1seek~1next/get
	def get_next(pod_name:str, table_name:str):

		return modules.get_next(pod_name, table_name, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Key-Value-Store/paths/~1kv~1loadcsv/post
	def load_csv(pod_name:str, table_name:str, memory:str):

		return modules.load_csv(pod_name, table_name, memory, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Key-Value-Store/paths/~1kv~1present/get
	def key_present(pod_name:str, table_name:str, key:str):

		return modules.key_present(pod_name, table_name, key, cookies = self.__cookies, host = self.__host)

	"""document functions"""

	#https://docs.modules.fairdatasociety.org/api/#tag/Document-DB/paths/~1doc~1new/post
	def create_documentDB(pod_name:str, table_name:str, si:str, mutable:bool):

		return modules.create_documentDB(pod_name, table_name, si, mutable, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Document-DB/paths/~1doc~1ls/get
	def list_documentDBs(pod_name:str):

		return modules.list_documentDBs(pod_name, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Document-DB/paths/~1doc~1open/post
	def open_documentDB(pod_name:str, table_name:str):

		return modules.open_documentDB(pod_name, table_name, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Document-DB/paths/~1doc~1count/post
	def count_documents(pod_name:str, table_name:str):

		return modules.count_documents(pod_name, table_name, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Document-DB/paths/~1doc~1delete/delete
	def delete_documentDB(pod_name:str, table_name:str):

		return modules.delete_documentDB(pod_name, table_name, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Document-DB/paths/~1doc~1find/get
	def find_documents(pod_name:str, table_name:str, expr:str, limit:int):

		return modules.find_documents(pod_name, table_name, expr, limit, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Document-DB/paths/~1doc~1loadjson/post
	def load_json(pod_name:str, table_name:str, filename:str):

		return modules.load_json(pod_name, table_name, filename, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Document-DB/paths/~1doc~1indexjson/post
	def index_json(pod_name:str, table_name:str, file:str):

		return modules.index_json(pod_name, table_name, file, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Document-DB/paths/~1doc~1entry~1put/post
	def put_document(pod_name:str, table_name:str, doc:str):

		return modules.put_document(pod_name, table_name, doc, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Document-DB/paths/~1doc~1entry~1get/get
	def get_document(pod_name:str, table_name:str, id:str):

		return modules.get_document(pod_name, table_name, id, cookies = self.__cookies, host = self.__host)

	#https://docs.modules.fairdatasociety.org/api/#tag/Document-DB/paths/~1doc~1entry~1del/delete
	def delete_document(pod_name:str, table_name:str, id:str):

		return modules.delete_document(pod_name, table_name, id, cookies = self.__cookies, host = self.__host)

if __name__ == '__main__':

	#some tests for functions
	
	fs = Fairos('http://localhost:9090')

	fs.signup_user('test', 'test')

	fs.login_user('test', 'test')

	res = fs.user_stat()
	print(res)

	res = fs.new_pod('mypod')
	print(res)

	res = fs.sync_pod('mypod')
	print(res)

	res = fs.share_pod('mypod')
	print(res)

	res = fs.list_pod()
	print(res)

	res = fs.stat_pod('mypod')
	print(res)

	res = fs.make_dir('mypod','tempdir')
	print(res)

	res =fs.list_dir('mypod')
	print(res)

	res = fs.stat_dir('mypod', 'tempdir')
	print(res)

	res = fs.user_logout()
	print(res)

	res = fs.create_new_table('mypod', 'mytable')
	print(res)

	res = fs.list_tables('mypod')
	print(res)

	res = fs.open_table('mypod', 'mytable')
	print(res)

	res = fs.count_table('mypod', 'mytable')
	print(res)

	res =fs.put_key_value('mypod', 'mytable', 'name', 'we are millions')
	print(res)

	res = fs.get_value('mypod', 'mytable', 'name')
	print(res)

	res = fs.key_present('mypod', 'mytable', 'user')
	print(res)

	res = fs.create_documentDB('mypod', 'mytable', 'first_name=string,age=number,tags=map', True)
	print(res)

	res = fs.list_documentDBs('mypod')
	print(res)

	res = fs.open_documentDB('mypod', 'mytable')
	print(res)

	res = fs.count_documents('mypod', 'mytable')
	print(res)