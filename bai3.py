# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:26:39 2024

@author: Le Thi Huyen Nga
"""

a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
if a <=0 or b <=0 :
    print("Vui lòng nhập số nguyên dương")
chia_lay_phan_nguyen = (a // b)
chia_lay_phan_du = (a % b )
print("Phần nguyên của a chia b là:", chia_lay_phan_nguyen )
print("Phần dư của a chia b là:", chia_lay_phan_du )
