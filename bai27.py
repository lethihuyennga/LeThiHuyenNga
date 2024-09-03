# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:07:03 2024

@author: le Thi Huyen Nga
"""

hinh = input("nhập vào hình (v),(n),(t):")
if hinh == 'v':
    canh = float(input("nhập chiều dài cạnh:"))
    chu_vi = 4*canh
    print("chu vu hình vuông là:", chu_vi)
    dien_tich = canh*canh
    print("diện tích hình vuông là:", dien_tich)  
elif hinh == 'n':
    rong = float(input("nhập chiều rộng:"))
    dai = float(input("nhập chiều dài:"))
    chu_vi = 2*(rong+dai)
    print("chu vi hình chữ nhật là:", chu_vi)
    dien_tich = dai*rong
    print("diện tích hình chữ nhật là:", dien_tich)
elif hinh == 't':
    ban_kinh = float(input("nhập bán kính:"))
    chu_vi = 2*3.14*ban_kinh
    print("chu vi hình tròn là:")
    dien_tich = 3.14*(ban_kinh*2)
    print("diện tích hình tròn là:", dien_tich)
else:
    print("hình không hợp lệ")