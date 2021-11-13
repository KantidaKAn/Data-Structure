'''
Chapter : 1 - item : 3 - Fun with permute
เขียนโปรแกรม Python เพื่อสร้างวิธีเรียงสับเปลี่ยนที่เป็นไปได้ทั้งหมดจากชุดตัวเลขที่กำหนด

'''

import math
Ans = []

def p(l):
    A = l.copy()
    Ans.append(A)
    B = l.copy()
    for j in range(0, len(l)-1):
        b = B[j]
        B[j] = B[j+1]
        B[j+1] = b
        C = B .copy()
        Ans.append(C)


def set(l):

    temp = l.copy()
    p(temp)
    for i in range(1, len(l)-1):
        for j in range(1, len(l)-1):
            b = temp[j]
            temp[j] = temp[j+1]
            temp[j+1] = b

            p(temp)
        b = temp[1]
        temp[1] = temp[len(l)-1]
        temp[len(l)-1] = b
        if i != len(l)-2:

            p(temp)


print("*** Fun with permute ***")
x = [int(j) for j in input("input : ").split(",")]
print(f'Original Cofllection:  {x}')
xr = x[::-1]
set(xr)
print(f'Collection of distinct numbers:\n {Ans}')
