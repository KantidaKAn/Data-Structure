'''
Chapter : 3 - item : 2 - Number in Stack

จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้

A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack

P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )

D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  

LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม

*** Hint ***

ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ

'''

class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def Value(self):
        return self.items

    def copy(self,l):
        self.items = l

    def castlisttoint(self):
        for i in range(len(self.items)):
            self.items[i]=int(self.items[i])

def manageStack(inp):
    S = Stack()

    def A(num):
        S.push(num)
        print("Add = "+str(num))

    def P():
        if S.size() > 0:
            p = S.pop()
            print("Pop = "+str(p))
        else:
            print("-1")

    def D(num):
        d = Stack()
        if S.size() > 0 :
            for i in S.Value():
                if i != num :
                    d.push(i)
                else :
                    print("Delete = "+str(num))
            S.copy(d.Value())
        else:
            print("-1")
    
    def LD(num):
        LD = Stack()
        li = S.Value()
        li.reverse()
        if S.size() > 0 :
            for i in li:
                if int(i) >= int(num) :
                    LD.push(i)
                else :
                    print("Delete = "+str(i)+" Because "+str(i)+" is less than "+str(num))
            LDlist = LD.Value()
            LDlist.reverse()
            S.copy(LDlist)
        else:
            print("-1")

    def MD(num):
        MD = Stack()
        li = S.Value()
        li.reverse()
        if S.size() > 0 :
            for i in li:
                if int(i) <= int(num) :
                    MD.push(i)
                else :
                    print("Delete = "+str(i)+" Because "+str(i)+" is more than "+str(num))
            MDlist = MD.Value()
            MDlist.reverse()
            S.copy(MDlist)
        else:
            print("-1")

    for i in inp :
        L = i.split()
        if L[0] == "A":
            A(L[1])
        elif L[0] == "P":
            P()
        elif L[0] == "D":
            D(L[1])
        elif L[0] == "LD":
            LD(L[1])
        elif L[0] == "MD":
            MD(L[1])
    S.castlisttoint()
    print("Value in Stack = "+str(S.Value()))
l = input("Enter Input : ").split(',')
manageStack(l)

