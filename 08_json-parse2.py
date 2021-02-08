# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.parse
import requests

main_api="https://www.mapquestapi.com/directions/v2/route?"
orig="Ibarra"
dest="Quito"
key="bw18sCGFDdK5DCYCzfz8x9hEqfjGCJgf"
url=main_api+urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
json_data=requests.get(url).json()
print(json_data)