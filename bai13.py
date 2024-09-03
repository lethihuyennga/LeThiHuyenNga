# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:00:04 2024

@author: Le Thi Huyen Nga
"""

ngày = int(input("Nhập ngày: "))
tháng = int(input("Nhập tháng: "))
năm = int(input("Nhập năm: "))

print(f"{ngày}/{tháng}/{năm}")

print(f"{ngày}/{tháng}/{str(năm)[-2:]}")

print(f"{năm}/{tháng}/{ngày}")

ngày, tháng, năm = map(int, input("Nhập lại theo định dạng ngày/tháng/năm: ").split('/'))

print(f"{ngày}/{tháng}/{năm}")

print(f"{ngày}/{tháng}/{str(năm)[-2:]}")

print(f"{năm}/{tháng}/{ngày}")