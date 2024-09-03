# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:00:38 2024

@author: Le Thi Huyen Nga
"""

#câu a
a = int(input("nhập số a:"))
b = int(input("nhập số b:"))
c = int(input("nhập số d:"))
min_value = min(a, b, c)
max_value = max(a, b, c)
mid_value = a + b + c - min_value - max_value
print("số theo thứ tự tăng dần: ", min_value, mid_value, max_value)

#câub
N = input("nhập số nguyên N: ")
Sap_xep_N = ''.join(sorted(N))
print("số có các con số theo thứ tự tăng dần: ", Sap_xep_N)