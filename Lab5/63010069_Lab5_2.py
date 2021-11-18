'''
Chapter : 5 - item : 2 - Doubly Linked List(append,insert,remove)
ให้เขียนคลาสของ Doubly Linked List ซึ่งมีเมท็อดดังนี้

1. def __init__(self): สำหรับสร้าง linked list

2. def __str__(self): return string แสดง ค่าใน linked list

3. def str_reverse(self): return string แสดง ค่าใน linked list จากหลังมาหน้า

4. def isEmpty(self): return list นั้นว่างหรือไม่

5. def append(self, data): add node ที่มี data เป็น parameter ข้างท้าย linked list

6. def insert(self, index, data): insert data ใน index ที่กำหนด

7. def remove(self, data): remove & return node ที่มี data

 - การแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่ 

คำแนะนำเพิ่มเติม เพื่อความง่ายในการเขียนโค้ดและไม่ต้องเขียนspecial caseเยอะๆ ให้ลองใช้ Dummy Node ดูนะครับ(หากสงสัยการใช้งาน Dummy Node สอบถามพี่ๆTA หรือ https://youtu.be/XgUIjTQ1HjA )

โดยรูปแบบ Input มีดังนี้
1. append       ->  A
2. add_before -> Ab
3. insert          ->   I
4. remove       ->  R

'''

class DoublyLinkedList:
    class Node:
        def __init__(self, data, prev=None, next=None):
            self.data = data
            if prev is None:
                self.prev = None
            else:
                self.prev = prev
            if next is None:
                self.next = None
            else:
                self.next = next

    def __init__(self):
        self.dummy = self.Node(None, None, None)
        self.dummy.next = self.dummy.prev = self.dummy
        self.size = 0

    def __str__(self):
        s = ''
        p = self.dummy.next
        for i in range(len(self)-1):
            s += str(p.data) + '->'
            p = p.next
        if str(p.data) != "None":
            s += str(p.data)
        return s

    def str_reverse(self):
        s = ''
        p = self.nodeAt(len(self)-1)
        for i in range(len(self)-1):
            s += str(p.data) + '->'
            p = p.prev
        if str(p.data) != "None":
            s += str(p.data)
        return s

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def indexOf(self, data):
        q = self.dummy.next
        for i in range(len(self)):
            if q.data == data:
                return i
            q = q.next
        return -1

    def isIn(self, data):
        return self.indexOf(data) >= 0

    def nodeAt(self, i):
        p = self.dummy
        for j in range(-1, i):
            p = p.next
        return p

    def insert(self, q, data):
        p = q.prev
        x = self.Node(data, p, q)
        p.next = q.prev = x
        self.size += 1

    def append(self, data):
        self.insert(self.nodeAt(len(self)), data)

    def remove(self, q):
        if self.isIn(q):
            q = self.nodeAt(self.indexOf(q))
            p = q.prev
            x = q.next
            p.next = x
            x.prev = p
            self.size -= 1
            return q
        else:
            return -1

    def delete(self, i):
        self.remove(self.nodeAt(i))


LL = DoublyLinkedList()
inp = input("Enter Input : ")
inp = inp.replace(", ", ",")
inp = inp.split(",")
for i in inp:
    num = i.split()
    command = num[0]
    if num[0] == 'A':
        LL.append(num[1])

    elif num[0] == 'Ab':
        LL.insert(LL.nodeAt(0), num[1])

    elif num[0] == 'I':
        index, data = num[1].split(":")

        if int(index) < 0 or len(LL) < int(index):
            print("Data cannot be added")

        else:
            LL.insert(LL.nodeAt(int(index)), data)
            print("index = {0} and data = {1}".format(index, data))

    elif num[0] == 'R':
        idx = LL.indexOf(num[1])
        r = LL.remove(num[1])

        if r == -1:
            print("Not Found!")

        else:
            print("removed : {0} from index : {1}".format(str(r.data), str(idx)))

    print("linked list : " + str(LL))
    
    print("reverse : "+LL.str_reverse())
