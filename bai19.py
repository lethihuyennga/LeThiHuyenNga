# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:24:59 2024

@author: le Thi Huyen Nga
"""

a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
c = int(input("Nhập vào số c: "))
d = int(input("Nhập vào số d: "))
if a <= b and a <= c and a <= d:
    So_be_nhat = a
elif b <= a and b <= c and b <= d:
    So_be_nhat = b
elif c <= a and c <= b and c <= d:
    So_be_nhat = c
else:
    So_be_nhat = d
print("Số bé nhất là: ", So_be_nhat)