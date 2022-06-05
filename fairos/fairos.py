#!/usr/bin/python3 
# -*- coding: utf-8 -*-
import os
import sys
import json
import requests

from .modules import db
from .modules import fs as filesystem
from .modules import kv
from .modules import pod
from .modules import user
from .modules import user_v2

class Fairos(object):
	"""docstring for Fairos"""
	def __init__(self, host = 'http://localhost:9090', version = 'v1'):
		super(Fairos, self).__init__()
		self.__host = host
		self.__cookies = None
		self.__user_name = ''
		self.__password = ''
		self.__version = version

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

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/User/paths/~1v1~1user~1signup/post
	def signup_user(self, user_name:str, password:str, mnemonic = ''):

		if self.__version == 'v2':
			return user_v2.signup_user(user_name, password, mnemonic = mnemonic, host = self.__host)

		return user.signup_user(user_name, password, mnemonic = mnemonic, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/User/paths/~1v1~1user~1login/post
	def login_user(self, user_name:str, password:str):

		if self.__version == 'v2':
			res = user_v2.login_user(user_name, password, host = self.__host)
		else:
			res = user.login_user(user_name, password, host = self.__host)

		if res['message'] == 'success':
			self.__user_name = user_name
			self.__password = password
			self.__cookies = res['cookies']

		return res

	#deprecated
	def import_user(self, user_name:str, password:str, address:str):

		res = user.import_user(user_name, password, address, host = self.__host)

		if res['message'] == 'success':
			self.__user_name = user_name
			self.__password = password
			self.__cookies = res['cookies']

		return res

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/User/paths/~1v2~1user~1migrate/post
	def migrate_user(self):

		return user_v2.migrate_user(self.__password, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/User/paths/~1v1~1user~1present/get
	def user_present(self, user_name:str):

		if self.__version == 'v2':
			return user_v2.user_present(user_name, host = self.__host)

		return user.user_present(user_name, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/User/paths/~1v1~1user~1isloggedin/get
	def is_logged_in(self, user_name:str):
		
		return user.is_logged_in(user_name, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/User/paths/~1v1~1user~1logout/post
	def user_logout(self):

		res = user.user_logout(cookies = self.__cookies, host = self.__host)	

		self.__cookies = None
		self.__user_name = ''
		self.__password = ''

		return res

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/User/paths/~1v1~1user~1export/post
	def export_user(self):

		return user.export_user(cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/User/paths/~1v1~1user~1delete/delete
	def delete_user(self, password:str):

		if self.__version == 'v2':
			res = user_v2.delete_user(password, cookies = self.__cookies, host = self.__host)
		else:
			res = user.delete_user(password, cookies = self.__cookies, host = self.__host)

		self.__cookies = None
		self.__user_name = ''
		self.__password = ''

		return res

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/User/paths/~1v1~1user~1stat/get
	def user_stat(self):

		return user.user_stat(cookies = self.__cookies, host = self.__host)

	"""pod functions """

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Pod/paths/~1v1~1pod~1receiveinfo/get
	def pod_receiveinfo(self, sharing_ref:str):

		return pod.pod_receiveinfo(sharing_ref, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Pod/paths/~1v1~1pod~1receive/get
	def pod_receive(self, sharing_ref:str):

		return pod.pod_receive(sharing_ref, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Pod/paths/~1v1~1pod~1new/post
	def new_pod(self, pod_name:str):

		return pod.new_pod(pod_name, self.__password, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Pod/paths/~1v1~1pod~1open/post
	def open_pod(self, pod_name:str):

		return pod.open_pod(pod_name, self.__password, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Pod/paths/~1v1~1pod~1close/post
	def close_pod(self, pod_name:str):

		return pod.close_pod(pod_name, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Pod/paths/~1v1~1pod~1sync/post
	def sync_pod(self, pod_name:str):

		return pod.sync_pod(pod_name, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Pod/paths/~1v1~1pod~1share/post
	def share_pod(self, pod_name:str):

		return pod.share_pod(pod_name, self.__password, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Pod/paths/~1v1~1pod~1delete/delete
	def delete_pod(self, pod_name:str):

		return pod.delete_pod(pod_name, self.__password, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Pod/paths/~1v1~1pod~1ls/get
	def list_pod(self):

		return pod.list_pod(cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Pod/paths/~1v1~1pod~1stat/get
	def stat_pod(self, pod_name:str):

		return pod.stat_pod(pod_name, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Pod/paths/~1v1~1pod~1present/get
	def pod_present(self, pod_name:str):

		return pod.pod_present(pod_name, cookies = self.__cookies, host = self.__host)

	"""filesystem functions"""

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/File-System/paths/~1v1~1dir~1mkdir/post
	def make_dir(self, pod_name:str, dir_path:str):

		dir_path = os.path.abspath(dir_path)

		return filesystem.make_dir(pod_name, dir_path, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/File-System/paths/~1v1~1dir~1rmdir/delete
	def remove_dir(self, pod_name:str, dir_path:str):

		dir_path = os.path.abspath(dir_path)

		return filesystem.remove_dir(pod_name, dir_path, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/File-System/paths/~1v1~1dir~1ls/get
	def list_dir(self, pod_name:str, dir_path:str):

		dir_path = os.path.abspath(dir_path)

		return filesystem.list_dir(pod_name, dir_path, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/File-System/paths/~1v1~1dir~1stat/get
	def stat_dir(self, pod_name:str, dir_path:str):

		dir_path = os.path.abspath(dir_path)

		return filesystem.stat_dir(pod_name, dir_path, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/File-System/paths/~1v1~1dir~1present/get
	def dir_present(self, pod_name:str, dir_path:str):

		dir_path = os.path.abspath(dir_path)

		return filesystem.dir_present(pod_name, dir_path, cookies = self.__cookies, host =self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/File-System/paths/~1v1~1file~1upload/post
	def upload_file(self, pod_name:str, dir_path:str, filename:str, block_size = '512'):

		dir_path = os.path.abspath(dir_path)

		return filesystem.upload_file(pod_name, dir_path, filename, block_size = block_size, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/File-System/paths/~1v1~1file~1download/get
	def download_file(self, pod_name:str, file_path:str, request_type = 'post'):

		return filesystem.download_file(pod_name, file_path, request_type = request_type, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/File-System/paths/~1v1~1file~1share/post
	def share_file(self, pod_name:str, pod_path_file:str, dest_user:str):

		return filesystem.share_file(pod_name, pod_path_file, dest_user, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/File-System/paths/~1v1~1file~1receive/get
	def receive_file(self, pod_name:str, sharing_ref:str, dir_path:str):

		dir_path = os.path.abspath(dir_path)

		return filesystem.receive_file(pod_name, sharing_ref, dir_path, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/File-System/paths/~1v1~1file~1receiveinfo/get
	def receive_file_info(self, pod_name:str, sharing_ref:str):

		return filesystem.receive_file_info(pod_name, sharing_ref, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/File-System/paths/~1v1~1file~1delete/delete
	def delete_info(self, pod_name:str, file_path:str):

		return filesystem.delete_info(pod_name, file_path, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/File-System/paths/~1v1~1file~1stat/get
	def stat_info(self, pod_name:str, file_path:str):

		return filesystem.stat_info(pod_name, file_path, cookies = self.__cookies, host = self.__host)

	"""kv functions """

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1kv~1new/post
	#indexType = 'string' or 'number'
	def create_new_table(self, pod_name:str, table_name:str, indexType = 'string'):

		return kv.create_new_table(pod_name, table_name, indexType, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1kv~1ls/get
	def list_tables(self, pod_name:str):

		return kv.list_tables(pod_name, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1kv~1open/post
	def open_table(self, pod_name:str, table_name:str):

		return kv.open_table(pod_name, table_name, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1kv~1count/post
	def count_table(self, pod_name:str, table_name:str):

		return kv.count_table(pod_name, table_name, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1kv~1delete/delete
	def delete_table(self, pod_name:str, table_name:str):

		return kv.delete_table(pod_name, table_name, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1kv~1entry~1put/post
	def put_key_value(self, pod_name:str, table_name:str, key:str, value:str):

		return kv.put_key_value(pod_name, table_name, key, value, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1kv~1entry~1get-data/get
	#format = '' or 'string' or 'byte-string'
	def get_value(self, pod_name:str, table_name:str, key:str, format = 'string'):

		return kv.get_value(pod_name, table_name, key, format = format, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1kv~1entry~1del/delete
	def delete_value(self, pod_name:str, table_name:str, key:str):

		return kv.delete_value(pod_name, table_name, key, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1kv~1seek/post
	def seek_key(self, pod_name:str, table_name:str, start_prefix:str, end_prefix = '', limit = 0):

		return kv.seek_key(pod_name, table_name, start, end, limit, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1kv~1seek~1next/get
	def get_next(self, pod_name:str, table_name:str):

		return kv.get_next(pod_name, table_name, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1kv~1loadcsv/post
	def load_csv(self, pod_name:str, table_name:str, csv:str, memory:str):

		return kv.load_csv(pod_name, table_name, csv, memory, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1kv~1present/get
	def key_present(self, pod_name:str, table_name:str, key:str):

		return kv.key_present(pod_name, table_name, key, cookies = self.__cookies, host = self.__host)

	"""document functions"""

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Document-DB/paths/~1v1~1doc~1new/post
	def create_documentDB(self, pod_name:str, table_name:str, si:str, mutable:bool):

		return db.create_documentDB(pod_name, table_name, si, mutable, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Document-DB/paths/~1v1~1doc~1ls/get
	def list_documentDBs(self, pod_name:str):

		return db.list_documentDBs(pod_name, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Document-DB/paths/~1v1~1doc~1open/post
	def open_documentDB(self, pod_name:str, table_name:str):

		return db.open_documentDB(pod_name, table_name, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Document-DB/paths/~1v1~1doc~1count/post
	def count_documents(self, pod_name:str, table_name:str, expr:str):

		return db.count_documents(pod_name, table_name, expr, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Document-DB/paths/~1v1~1doc~1delete/delete
	def delete_documentDB(self, pod_name:str, table_name:str):

		return db.delete_documentDB(pod_name, table_name, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Document-DB/paths/~1v1~1doc~1find/get
	def find_documents(self, pod_name:str, table_name:str, expr:str, limit:int):

		return db.find_documents(pod_name, table_name, expr, limit, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1doc~1loadjson/post
	def load_json(self, pod_name:str, table_name:str, json:str):

		return db.load_json(pod_name, table_name, json, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1doc~1indexjson/post
	def index_json(self, pod_name:str, table_name:str, file:str):

		return db.index_json(pod_name, table_name, file, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1doc~1entry~1put/post
	def put_document(self, pod_name:str, table_name:str, doc:str):

		return db.put_document(pod_name, table_name, doc, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1doc~1entry~1get/get
	def get_document(self, pod_name:str, table_name:str, id:str):

		return db.get_document(pod_name, table_name, id, cookies = self.__cookies, host = self.__host)

	#https://docs.fairos.fairdatasociety.org/api/index.html#tag/Key-Value-Store/paths/~1v1~1doc~1entry~1del/delete
	def delete_document(self, pod_name:str, table_name:str, id:str):

		return db.delete_document(pod_name, table_name, id, cookies = self.__cookies, host = self.__host)