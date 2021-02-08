# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:25:17 2021

@author: mmant
"""

aclNum=int(input("What is the IPv4 ACL number? "))
if aclNum>= 1 and aclNum<=99:
    print("\n This is a standard IPv4 ACL.")
elif aclNum>= 100 and aclNum<=199:
    print("\n This is a extended IPv4 ACL.")
else:
    print("\n This is not a standard or extended IPv4 ACL.")