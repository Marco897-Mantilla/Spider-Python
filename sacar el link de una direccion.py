# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 07:27:12 2021

@author: mmant
"""
import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "bw18sCGFDdK5DCYCzfz8x9hEqfjGCJgf"
# The "while true" construct creates an endless loop
while True:
    oring = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from":oring, "to":dest})
    print("URL: " + (url))