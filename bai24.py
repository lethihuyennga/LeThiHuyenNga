# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:30:02 2024

@author: PC
"""

h = int(input("nhập giờ:"))
p = int(input("nhập phút:"))
s = int(input("nhập giây:"))
if 0<=h<=23 and 0<=p<=59 and 0<=s<=59:
    print("thời gian hợp lệ")
else:
    print("thời gian không hợp lệ")
    