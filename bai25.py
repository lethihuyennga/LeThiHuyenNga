# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:52:01 2024

@author: le Thi Huyen Nga 
"""

ch = input("nhập một chữ cái:")
if ch.islower():
    ch = ch.upper()
else:
    ch = ch.lower()
print("kết quả", ch)
