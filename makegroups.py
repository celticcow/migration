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
def create_group():
    pass

"""
main function
"""
def main():
    grpdate = set()

    grpdata = importdata('EAI_PGH2LAS.csv') #EAI_PGH2LAS.csv

    for grp in grpdata:
        grp.print_appgroup()

if __name__ == "__main__":
    main()