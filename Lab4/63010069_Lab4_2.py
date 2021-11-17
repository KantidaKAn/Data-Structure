'''
Chapter : 4 - item : 2 - แถวคอย

จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue

โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้

แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ

แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ

ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2

จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2]

'''

class Queue :
    def __init__(self) :
        self.items = []

    def Enqueue(self, value) :
        self.items.append(value)

    def Dequeue(self) :
        if not self.isEmpty() :
            return self.items.pop(0)
        return -1

    def isEmpty(self) :
        return self.size() == 0
        
    def size(self) :
        return len(self.items)

    def getQueue(self) :
        return self.items

if __name__ == '__main__' :
    p, t = input('Enter people and time : ').split()
    t = int(t)
    q1, q2, q3 = Queue(), Queue(), Queue()
    for i in p : q1.enqueue(i)
    t1 = t2 = 0
    for i in range(1, t + 1) :
        if t1 % 3 == 0 and not q2.isEmpty():
            q2.dequeue()
            t1 = 0
        if t2 % 2 == 0 and not q3.isEmpty() :
            q3.dequeue()
            t2 = 0

        if q2.size() < 5 and not q1.isEmpty()   : q2.enqueue(q1.dequeue())
        elif q3.size() < 5 and not q1.isEmpty() : q3.enqueue(q1.dequeue())
        if not q2.isEmpty() : t1 += 1
        if not q3.isEmpty() : t2 += 1
        
        print(f'{i} {q1.getQueue()} {q2.getQueue()} {q3.getQueue()}')