# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:47:58 2024

@author: le Thi Huyen Nga
"""

hh = int(input("Nhập giờ: "))
mm = int(input("Nhập phút: "))
ss = int(input("Nhập giây: "))
tong_giay = hh * 36000 + mm * 60 + ss
print("Tổng số giây là:", tong_giay)