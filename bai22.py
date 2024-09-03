# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:49:16 2024

@author: le Thi Huyen Nga
"""

a = int(input("nhập số a:"))
b = int(input("nhập số b:"))
if a!=0:
    print("phương trình có nghiệm x=", -b/a)
else:
    if b!=0:
        print("phương trình vô nghiệm")
    else: print("phương trình có vô số nghiệm")