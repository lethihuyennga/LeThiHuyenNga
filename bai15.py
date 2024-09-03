# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:13:12 2024

@author: le Thi Huyen Nga
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
A = ((a+b)/(a**(1/3)+b**(1/3))) - (a*b)**(1/3)
B = (a**(1/3) - b**(1/3))**2
print("Kết quả: ", A/B )