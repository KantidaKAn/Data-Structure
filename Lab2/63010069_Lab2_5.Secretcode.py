'''
Chapter : 2 - item : 5 - รหัสลับ
ตึกลึกลับแห่งหนึ่งเมื่อเดินไปข้างหลังจะมีคนบอกรหัสลับมาจงสร้างฟังชั่นคำนวณรหัส
โดยรหัสจะประกอบไปด้วย english word that have repeat character
เช่น bon("ball") = 48 หรือ bon("aah") = 4

'''
from collections import defaultdict

char = "abcdefghijklmnopqrstuvwxyz"
def duplicates(st):
 count = defaultdict(int)
 for i in range(len(st)):
    count[st[i]] += 1
 for j in count:
      if (count[j] > 1):
        return j

def bon(w):
    x = int(0)
    for i in char:
        x += 1
        if i == w:
            return x*4

in_put = input("Enter secret code : ")
print(bon(duplicates(in_put)))