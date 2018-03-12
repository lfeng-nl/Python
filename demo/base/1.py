#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

#    输入体重和身高，计算BMI值，并判断肥胖情况


height = float(input("please input height(m): "))
weight = float(input("please input weight(kg): "))

bmi = weight / (height**2)
print("bmi = %f" % bmi)

if bmi < 18.5:
    print("过轻")
elif 18.5 <= bmi < 25:
    print("正常")
elif 25 <= bmi < 28:
    print("过重")
elif 28 <= bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")