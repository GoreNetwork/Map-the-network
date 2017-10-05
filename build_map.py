from common_functions import *
from cdp_work import *
from pprint import pprint


def make_dir_of_cdp_info():
	
	all_cdp_info = []
	cdp_files = pull_file_names_with_text("show cdp")
	for cdp_file in cdp_files:
		temp_dir = parse_cdp_out(cdp_file)
		all_cdp_info.append(temp_dir)
	all_cdp_info = get_rid_of_dups(all_cdp_info)
	#for each in all_cdp_info:
	#	pprint (each)
	
	
	
	
	for cdp_neighborship in all_cdp_info:
		pprint (cdp_neighborship)
		if ("SEP" not in cdp_neighborship['local_host_name']) and ("SEP" not in cdp_neighborship['remote_id']):
			if "&" in cdp_neighborship['local_host_name']:
				#print ("Local_host_Hit")
				cdp_neighborship['local_host_name']=cdp_neighborship['local_host_name'].replace("&","&amp;")
			if "&" in cdp_neighborship['remote_id']:
				#print ("Local_host_Hit")
				cdp_neighborship['remote_id']=cdp_neighborship['remote_id'].replace("&","&amp;")
			write_me = cdp_neighborship['local_host_name']+","+cdp_neighborship['remote_id']+","+cdp_neighborship['local_int']+","+cdp_neighborship['remote_int']+"\n"
			to_doc_a("results.csv",write_me)
	
	
	return all_cdp_info
		
def get_rid_of_dups(original_all_cdp_info):
	no_dups_all_cdp_info = []
	for org_cdp_list in original_all_cdp_info:
		for org_cdp_dir in org_cdp_list:
			add = True
			for no_dup_dir in no_dups_all_cdp_info:
				#print (no_dup_dir['remote_id'])
				#print (org_cdp_dir['local_host_name'])
				#print (org_cdp_dir)
				#print (org_cdp_dir['local_host_name'])
				#print (no_dup_dir['remote_id'])
				if org_cdp_dir['local_host_name'] == no_dup_dir['remote_id']:
					if org_cdp_dir['local_int'] == no_dup_dir['remote_int']:
						if org_cdp_dir['remote_int'] == no_dup_dir['local_int']:
							add = False
							#print ("this_was_a_dup")
			if add == True:
				no_dups_all_cdp_info.append(org_cdp_dir)
	return no_dups_all_cdp_info

to_doc_w("results.csv","")	
make_dir_of_cdp_info()
from yEd_work import *


