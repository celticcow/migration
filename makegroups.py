#!/usr/bin/python3 -W ignore::DeprecationWarning

import requests
import json
import sys
import csv
import time
import getpass
import ipaddress
import apifunctions

from appgroup import appgroup

#remove the InsecureRequestWarning messages
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""
gregory.dunlap / celtic_cow

create a set of objects of type app-group
"""

"""
take data from csv of move groups and ouput data file we can use for import and do some sanitation of data

85768	CMP - DEVELOPMENT	Development	LAS
85768	CMP - TEST	Test	LAS

turn into group : name - LAS-eai-85768-Development
                  color - brown
                  comment - "CMP Development"

                  name - LAS-eai-85768-Test
                  color - brown
                  comment - "CMP Test"
"""
## read csv file and create a uniq set of grp data
def importdata(filename):
    print("in function importdata()")
    movewaves = set()

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            tmp_eai_id = row[1]
            tmp_comment = row[2]
            tmp_instance = row[3]
            tmp_dc = row[4]

            tmp_group = appgroup(tmp_dc, tmp_eai_id, tmp_instance, tmp_comment)
            
            if(len(movewaves) == 0):
                movewaves.add(tmp_group)
            else:
                exist = 0
                for item in movewaves:
                    if(item.get_name() == tmp_group.get_name()):
                        exist = 1
                
                if(exist == 0):
                    movewaves.add(tmp_group)

    return(movewaves)

"""
make group
"""
def create_group(appgroup, ip_addr, sid):
    print("In function create_group()")
    debug = 1

    if(apifunctions.group_exist(ip_addr, appgroup.get_name(), sid) == False):
        if(appgroup.get_level() == "Production"):
            color = "crete blue"
        else:
            color = "brown"

        newgrp_json = {
            "name" : appgroup.get_name(),
            "color" : color,
            "comments" : appgroup.get_comment()
        }

        add_result = apifunctions.api_call(ip_addr, "add-group", newgrp_json, sid)

        print(json.dumps(add_result))

"""
main function
"""
def main():
    debug = 1

    grpdate = set()

    grpdata = importdata('EAI_PGH2LAS.csv') #EAI_PGH2LAS.csv

    ip_addr = input("enter IP of MDS : ")
    ip_cma  = input("enter IP of CMA : ")
    user    = input("enter P1 user id : ")
    password = getpass.getpass('Enter P1 Password : ')

    sid = apifunctions.login(user, password, ip_addr, ip_cma)

    if(debug == 1):
        print("session id : " + sid)
    #do mds login here

    publish_counter = 0

    for grp in grpdata:
        print("EXP : ", end='')
        grp.print_appgroup()
        create_group(grp, ip_addr, sid)
        publish_counter += 1
        
        if(publish_counter == 50):
            ##call publish
            print("incremental publish")
            time.sleep(10)
            publish_result = apifunctions.api_call(ip_cma, "publish", {}, sid)
            print("publish results : " + json.dumps(publish_result))
            time.sleep(20)
            publish_counter = 0
    
    ## Publish pending changes
    print("Start of Publish ... zzzzz")
    time.sleep(10)
    publish_result = apifunctions.api_call(ip_cma, "publish", {}, sid)
    print("publish results : " + json.dumps(publish_result))

    time.sleep(10)

    ## Logout
    logout_result = apifunctions.api_call(ip_addr, "logout", {}, sid)
    if(debug == 1):
        print(logout_result)
#end of main()

if __name__ == "__main__":
    main()