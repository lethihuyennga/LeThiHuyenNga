# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:07:21 2024

@author: le Thi Huyen Nga
"""

can_nang = float(input("Nhập số cân nặng (kg): "))
chieu_cao = float(input("Nhập số chiều cao (m): "))
cong_thuc_BMI = can_nang / (chieu_cao*2)
print("Tính số đo kiểm tra sức khỏe BMI: ", cong_thuc_BMI)