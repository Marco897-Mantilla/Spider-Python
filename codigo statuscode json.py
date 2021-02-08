# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 08:34:31 2021

@author: mmant
"""

import urllib.parse
import requests

main_api="https://www.mapquestapi.com/directions/v2/route?"
orig="Ibarra"
dest="Quito"
key="bw18sCGFDdK5DCYCzfz8x9hEqfjGCJgf"
url=main_api+urllib.parse.urlencode({"key":key,"from":orig,"to":dest})


print("URL: "+ (url))

json_data=requests.get(url).json()
json_status=json_data["info"]["statuscode"]

if json_status==0:
    print("API Status: "+str(json_status)+"= A successful rote call. \n")