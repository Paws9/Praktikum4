# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:12:18 2022

@author: zakyf
"""
x=int(input("masukan jumlah bilangan: "))
for i in range(x,0,-1):
    num=i
    for z in range(i):
        print(num, end="")
    print("\n")