'''
Chapter : 6 - item : 5 - วาดภาพแสนสุข

เขียนโปรแกรมที่แสดงผลดังตัวอย่าง

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

def staircase(n):
    #code here

print(staircase(int(input("Enter Input : "))))
'''
def draw(drawing,end):
    if end>0:
        print('_'*(end-1)+'#'*(drawing))
        draw(drawing+1,end-1)
    elif end<0:
        print('_'*drawing+'#'*(end*-1))
        draw(drawing+1,end+1)
num = input("Enter Input : ")
num = int(num)
if num > 0:
    draw(1,num)
elif num < 0:
    draw(0,num)
else:
    print("Not Draw!")