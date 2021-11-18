'''
Chapter : 5 - item : 3 - รวม Linked List
ให้น้องรับ Linked List มา 2 ตัว จากนั้นนำ 2 Linked List มาต่อกัน โดย L2 จะมาต่อ L1 แบบกลับหลัง

'''

class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.siz = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head is None:
            self.head = self.Node(item)
            self.siz += 1
        else:
            p = self.head
            for i in range(0,self.siz-1):
                p = p.next
            q = self.Node(item)
            p.next = q
            self.siz += 1

    def appendNode(self,node):
        p = self.head
        for i in range(0,self.siz-1):
            p = p.next
        p.next = node
        self.siz += 1

    def addHead(self, item):
        if self.isEmpty():
            p = self.Node(item)
            self.head = p
            self.siz += 1
        else:
            p = self.Node(item)
            p.next = self.head
            self.head = p
            self.siz += 1

    def search(self, item):
        if self.index(item)>=0:
            return "Found"
        else:
            return "Not Found"

    def index(self, item):
        p=self.head
        for i in range(self.size()):
            if p.value == item:
                return i
            p = p.next
        return -1

    def size(self):
        return self.siz

    def pop(self, pos):
        if pos < 0 or pos >= self.siz:
            return "Out of Range"
        if pos == 0 and self.siz > 0:
            self.head = self.head.next
            self.siz -= 1
            return "Success"
        else:
            p = self.head
            for i in range(0,pos-1):
                p = p.next 
            p.next =p.next.next
            self.siz -= 1
            return "Success"
    
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
 
    def returnhead(self):
        return self.head


llist = LinkedList()
L1, L2 = input('Enter Input (L1,L2) : ').split()
L1 = L1.split('->')
L2 = L2.split('->')
ll1 = LinkedList()
ll2 = LinkedList()
for i in L1:
    ll1.append(i)

for i in L2 :
    ll2.append(i)

print('L1    : '+str(ll1))
print('L2    : '+str(ll2))
ll2.reverse()
ll1.appendNode(ll2.returnhead())
print('Merge : '+str(ll1))
