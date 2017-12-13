import os
import re
import socket
import sys
import netmiko
from getpass import getpass
from ciscoconfparse import CiscoConfParse
from pprint import pprint

def read_doc_str(file_name):
	my_file = open(file_name,"r")
	return (my_file.read())

def pull_file_names_with_text(text):
	file_list = []
	files = os.listdir()
	for file in files:
		if text in file:
			file_list.append(file)
	return (file_list)

def read_devices (file_name):
	my_devices = []
	for line in open(file_name, 'r').readlines():
		if get_ip(line):
			for each in get_ip(line): 
				my_devices.append(each)
	return my_devices
def get_mac (input):
	return(re.findall(r'(?:[0-9a-fA-F].?){12}', input))

def get_ip (input):
	return(re.findall(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', input))
	
def read_doc(file_name):
	doc = []
	for line in open(file_name, 'r').readlines():
		doc.append(line)
	return doc

def to_doc_w(file_name, varable):
	f=open(file_name, 'w')
	f.write(varable)
	f.close()	

def to_doc_a(file_name, varable):
	f=open(file_name, 'a')
	f.write(varable)
	f.close()	

def remove_start(line,remove_this):
	line_search = re.search(remove_this,line)
	line = line[line_search.end()+1:]
	return line
	
def make_list_string_with_spaces(list):
	line = str(list)
	line = line.replace("[","")
	line = line.replace("]","")
	line = line.replace(","," ")
	line = line.replace("'"," ")
	return line
	
	
def make_connection (ip,username,password,cant_connect):
	
	try:
		return netmiko.ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=password)
	except:
		try:
			return netmiko.ConnectHandler(device_type='cisco_ios_telnet', ip=ip, username=username, password=password)
		except:
			cant_connect.append(ip)
			issue = ip+ ", can't be ssh/telneted to"
			to_doc_a("Issues.csv", issue)
			to_doc_a("Issues.csv", "\n")
			
			for each in cant_connect:
				to_doc_a("cant_connect.txt", each)
				to_doc_a("cant_connect.txt", "\n")
			return cant_connect
		
def send_show_command(net_connect,command):
	return net_connect.send_command_expect (command)
			
def find_child_text (file, text):
	all = []
	parse = CiscoConfParse(file)
	for obj in parse.find_objects(text):
		each_obj = []
		each_obj.append(obj.text)
		for each in obj.all_children:
			each_obj.append(each.text)
		all.append(each_obj)
	return all
	
def remove_start(line,remove_this):
	line_search = re.search(remove_this,line)
	line = line[line_search.end()+1:]
	return line
	
def remove_end(line,remove_this):
	line_search = re.search(remove_this,line)
	line = line[:line_search.start()]
	return line


