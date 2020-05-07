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

def main():
    pass

if __name__ == "__main__":
    main()