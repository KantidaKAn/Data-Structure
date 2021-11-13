''' 
Chapter : 1 - item : 1 - radius and area of circle
เขียนโปรแกรม Python ซึ่งรับ input เป็นรัศมีของวงกลม จากนั้นคำนวณพื้นที่และแสดงผล 

'''

import math

radius = float(input("r="))
print("Area=" + str(math.pi * radius**2))
