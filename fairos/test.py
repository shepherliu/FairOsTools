#!/usr/bin/python3 
# -*- coding: utf-8 -*-
import os
import sys
import json
import requests

from . import fairos

def test():

	#some tests for functions
	fs = fairos.Fairos('https://fairos.fairdatasociety.org')

	print('test signup user')
	res = fs.signup_user('test-swarm1', 'test-swarm1')
	print(res)
	res = fs.signup_user('test-swarm2', 'test-swarm2')
	print(res)
	res = fs.signup_user('test-swarm3', 'test-swarm3')
	print(res)	

	try:
		address = res['data']['address']
	except:
		address = '0x65Fc06282509881279a5C75C9aD4cD3Bc2714169'

	print('test login user')
	res = fs.login_user('test-swarm1', 'test-swarm1')
	print(res)

	print('test import user')
	res = fs.import_user('test-swarm2', 'test-swarm2', address)
	print(res)

	print('test user present')
	res = fs.user_present('test-swarm1')
	print(res)

	print('test user is logined in')
	res = fs.is_logged_in('test-swarm1')
	print(res)

	print('test user logout')
	res = fs.user_logout()
	print(res)

	res = fs.login_user('test-swarm1', 'test-swarm1')
	print('test export user')
	res = fs.export_user()
	print(res)

	print('test delete user')
	res = fs.delete_user('test-swarm1')
	print(res)

	res = fs.login_user('test-swarm2', 'test-swarm2')
	print('test user stat')
	res = fs.user_stat()
	print(res)

	print('test create new pod')
	res = fs.new_pod('pod1')
	print(res)
	res = fs.new_pod('pod2')
	print(res)
	res = fs.new_pod('pod3')
	print(res)

	print('test open pod')
	res = fs.open_pod('pod1')
	print(res)

	print('test close pod')
	res = fs.close_pod('pod1')
	print(res)

	res = fs.open_pod('pod1')
	print('test sync pod')
	res = fs.sync_pod('pod1')
	print(res)

	print('test share pod')
	res = fs.share_pod('pod1')
	pod_sharing_reference = res['data']['pod_sharing_reference']
	print(res)

	#test failed for not found, bugs
	print('test delete pod')
	res = fs.delete_pod('pod2')
	print(res)

	print('test list pod')
	res = fs.list_pod()
	print(res)

	print('test stat pod')
	res = fs.stat_pod('pod1')
	print(res)

	print('test pod present')
	res = fs.pod_present('pod3')
	print(res)

	res = fs.login_user('test-swarm3', 'test-swarm3')
	print('test pod receive info')
	res = fs.pod_receiveinfo(pod_sharing_reference)
	print(res)

	print('test pod receive')
	res = fs.pod_receive(pod_sharing_reference)
	print(res)

	res = fs.login_user('test-swarm2', 'test-swarm2')
	res = fs.open_pod('pod1')
	print('test mkdir')
	res = fs.make_dir('pod1', '/test')
	print(res)
	res = fs.make_dir('pod1', '/test/dir')
	print(res)

	print('test remove dir')
	res = fs.remove_dir('pod1', '/test/dir')
	print(res)

	res = fs.make_dir('pod1', '/test/test')
	res = fs.make_dir('pod1', '/test/dir2')
	res = fs.make_dir('pod1', '/test/dir3')

	print('test stat dir')
	res = fs.stat_dir('pod1', '/test/test')
	print(res)

	print('test dir present')
	res = fs.dir_present('pod1', '/test/test')
	print(res)

	print('test upload file')
	res = fs.upload_file('pod1', '/test/test', '/tmp/test.txt')
	print(res)

	print('test list dir')
	res = fs.list_dir('pod1', '/test/test')
	print(res)	

	print('test download file')
	res = fs.download_file('pod1', '/test/test/test.txt')
	print(res)

	# print('test share file')
	# res = fs.share_file('pod1', '/test/test/test.txt', 'test-swarm3')
	# print(res)

	# try:
	# 	file_sharing_reference = res['data']['file_sharing_reference']
	# except:
	# 	file_sharing_reference = ''

	# res.login_user('test-swarm3', 'test-swarm3')
	# print('test receive file')
	# res = fs.receive_file('pod1', file_sharing_reference, '/')
	# print(res)

	# print('test receive file info')
	# res = fs.receive_file_info('pod1', file_sharing_reference)
	# print(res)

	# print('test stat info')
	# res = fs.stat_info('pod1', '/test/test.txt')
	# print(res)

	# print('test delete info')
	# res = fs.delete_info('pod1', '/test/test.txt')
	# print(res)

	print('test create new table')
	res = fs.create_new_table('pod1', 'test_table')
	print(res)
	res = fs.create_new_table('pod1', 'test_table2')
	res = fs.create_new_table('pod1', 'test_tabl3')

	print('test list tables')
	res = fs.list_tables('pod1')
	print(res)

	print('test open table')
	res = fs.open_table('pod1', 'test_table')
	print(res)

	print('test delete table')
	res = fs.delete_table('pod1', 'test_table2')
	print(res)

	print('test put key value')
	res = fs.put_key_value('pod1', 'test_table', 'test_key', 'test_value')
	print(res)
	res = fs.put_key_value('pod1', 'test_table', 'test_key', 'test_value2')
	print(res)
	res = fs.put_key_value('pod1', 'test_table', 'test_key2', 'test_value2')
	print(res)
	res = fs.put_key_value('pod1', 'test_table', 'test_key3', 'test_value3')
	print(res)

	print('test get value')
	res = fs.get_value('pod1', 'test_table', 'test_key')
	print(res)
	res = fs.get_value('pod1', 'test_table', 'test_key2')
	print(res)

	print('test delete value')
	res = fs.delete_value('pod1', 'test_table', 'test_key2')
	print(res)

	print('test count table')
	res = fs.count_table('pod1', 'test_table')
	print(res)	
	
	print('test seek key')
	res = fs.seek_key('pod1', 'test_table', 'test_')
	print(res)

	print('test get next')
	res = fs.get_next('pod1', 'test_table')
	print(res)
	res = fs.get_next('pod1', 'test_table')
	print(res)
	res = fs.get_next('pod1', 'test_table')
	print(res)

	print('test key present')
	res = fs.key_present('pod1', 'test_table', 'test_key')
	print(res)

	print('test load csv')
	res = fs.load_csv('pod1', 'test_table', '/tmp/test.csv', 'memory')
	print(res)

	print('test create doc db')
	res = fs.create_documentDB('pod1', 'test-doc', 'firsr_name=string,age=number,tags=map', True)
	print(res)

	print('test list doc')
	res = fs.list_documentDBs('pod1')
	print(res)

	print('test open doc')
	res = fs.open_documentDB('pod1', 'test-doc')
	print(res)

	print('test count doc')
	res = fs.count_documents('pod1', 'test-doc', '')
	print(res)

	print('test find doc')
	res = fs.find_documents('pod1', 'test-doc', '', 0)
	print(res)

	print('load json')
	res = fs.load_json('pod1', 'test-doc', '/tmp/test.json')
	print(res)

	print('index json')
	res = fs.index_json('pod1', 'test-doc', 'test.json')
	print(res)

	print('test put doc')
	res = fs.put_document('pod1', 'test-doc', '/test.pdf')
	print(res)

	print('test get doc')
	res = fs.get_document('pod1', 'test-doc', '/test.pdf')
	print(res)

	print('test delete doc')
	res = fs.delete_document('pod1', 'test-doc', '/test.pdf')
	print(res)

	print('test delete doc db')
	res = fs.delete_documentDB('pod1', 'test-doc')
	print(res)		

if __name__ == '__main__':

	test()	
