'''
Chapter : 4 - item : 1 - Basic Queue
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา

E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผลค่าที่ทำการ enqueue และ index ของตัวที่ทำการเพิ่มเข้าไป

D           ให้ทำการ dequeue ตัวที่อยู่หน้าสุดของ Queue ออกและแสดงตัวเลขที่เอาออกและแสดงขนาดของ Queue

            หลังจากทำการ dequeue แล้ว

*** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty ***

'''

class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def Enqueue(self, value):
        self.items.append(value)

    def Dequeue(self):
        return self.items.pop(0)

    def Size(self):
        return len(self.items)

    def Value(self):
       return self.items

inp = input("Enter Input : ").split(',')
S = Queue()
for i in inp:
    L = i.split()
    if L[0] == 'E':
        S.Enqueue(L[1])
        print("Add " + str(L[1]) + " index is "+str(S.Size()-1))
    elif L[0] == 'D':
        if S.Size() > 0:
            P = S.Dequeue()
            print("Pop " + str(P) + " size in queue is "+str(S.Size()))
        else:
            print("-1")

if S.Size() == 0:
    print("Empty")
else:
    print("Number in Queue is :  ", end="")
    print(str(S.Value()))
    