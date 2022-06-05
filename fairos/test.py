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

	res = fs.signup_user('loveswarm', 'loveswarm')
	print(res)

	res = fs.login_user('loveswarm', 'loveswarm')
	print(res)

	res = fs.user_stat()
	print(res)

	res = fs.new_pod('mypod')
	print(res)

	res = fs.open_pod('mypod')
	print(res)

	res = fs.sync_pod('mypod')
	print(res)

	res = fs.share_pod('mypod')
	print(res)

	res = fs.list_pod()
	print(res)

	res = fs.stat_pod('mypod')
	print(res)

	res = fs.make_dir('mypod','/tempdir')
	print(res)

	res =fs.list_dir('mypod', '/tempdir')
	print(res)

	res = fs.stat_dir('mypod', '/tempdir')
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

	res = fs.count_documents('mypod', 'mytable', '')
	print(res)

	res = fs.close_pod('mypod')
	print(res)

	res = fs.user_logout()
	print(res)	

if __name__ == '__main__':

	test()	
