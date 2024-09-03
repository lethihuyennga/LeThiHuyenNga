# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:37:55 2024

@author: le Thi Huyen Nga
"""

n=int(input("Nhập biển số xe của bạn: "))
n=str(n) ; s=0
for i in range(len(n)) :
    s+=int(n[i])
print("Biển số xe của bạn có số nút là :", s%10)