# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:46:50 2021

@author: mmant
"""

import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "bw18sCGFDdK5DCYCzfz8x9hEqfjGCJgf"
# The "while true" construct creates an endless loop
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: "+str(json_status)+" = A successful route call.\n")
        print("Directions from "+ (orig) + " to " + (dest))
        print("Trip Duration: " + str(json_data["route"]["formattedTime"]))
        print("Miles:         " + str(json_data["route"]["distance"]))
        print("Fuel(Gal):     " + str(json_data["route"]["fuelUsed"]))
        print("============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + "Km"))
            print("===========================================\n")
            
        elif json_status == 402:
            print("*******************************************")
            print("For Status Code:  " + str(json_status) + "; Invalid user inputs for one or both locations.")
            print("***********************************************")
            
            else:
                print("******************************************")
                print("Status Code: " + str(json_status) + "; Refer to: ")
                print("https://developer.mapquest.com/documentation/directions-api/status-codes")
                print("*********************************************\n")