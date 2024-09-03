# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:27:45 2024

@author: Le Thi Huyen Nga
"""

a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
c = int(input("Nhập vào số c: "))
if a >= b and a >= c:
    So_lon_nhat = a
elif b >= a and b >=c:
    So_lon_nhat = b
else:
        So_lon_nhat = c
print("Số lớn nhất là: ", So_lon_nhat)