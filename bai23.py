# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:26:16 2024

@author: le Thi Huyen Nga
"""

a =float(input("Nhập a:"))
b =float(input("Nhập b:"))
c =float(input("Nhập c:"))
delta = b*b - 4*a*c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có một  nghiệm kép: x1 = x2 = ", -b/(2*a))
else: import math
x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)
print("Phuong trình có 2 nghiệm phân biệt: ")
print("x1 = ", x1, "x2 = ", x2)