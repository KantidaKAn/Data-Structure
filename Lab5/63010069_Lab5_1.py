'''
Chapter : 5 - item : 1 - Locomotive-(101)
มีรถไฟอยู่ขบวนหนึ่ง โดยรถไฟนั้นจะมีหมายเลขกำกับตู้แต่ละตู้อยู่และรถไฟก็มีหัวรถจักรอยู่

แต่หัวรถจักรดันไปต่อกับตู้รถไฟอยู่ พี่ต้องการให้น้อง ๆ ทำการแบ่งขบวนรถไฟออก

โดยให้หัวรถจักรอยู่ข้างหน้าสุด และส่วนตู้ที่เหลือให้ทำการต่อกับตู้สุดท้ายโดยไม่มีการเปลี่ยนลำดับของตู้

ซึ่งพี่จะให้หมายเลข 0 แทนเป็นหัวรถจักร ส่วน หมายเลขอื่นจะเป็นตู้รถไฟ

เช่น 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6

เป็น 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1 ( ให้ใช้ singly linked list)

 *** Locomotive ***
Enter Input : 2 3 1 0 4 5 6
Before : 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6
After : 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1

 *** Locomotive ***
Enter Input : 1 2 3 0
Before : 1 <- 2 <- 3 <- 0
After : 0 <- 1 <- 2 <- 3

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
        cur, s = self.head, str(self.head.value) + " <- "
        while cur.next.next != None:
            s += str(cur.next.value) + " <- "
            cur = cur.next
        s += str(cur.next.value)
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
        while(p.next != None):
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

    def NodeAt(self,index):
        p = self.head
        for i in range(index):
            p = p.next
        return p

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

    def changehead(self,nh):
        self.head = nh

print(' *** Locomotive ***')
inp = input('Enter Input : ').split()
ll = LinkedList()
for i in inp:
    ll.append(i)
print("Before : "+str(ll))
temphead = ll.returnhead()
siz  = ll.size()
if int(temphead.value) != 0:
    for i in range(siz):
        if int(ll.NodeAt(i).next.value) == 0 :
            nh = ll.NodeAt(i).next
            ll.NodeAt(i).next = None
            ll.changehead(nh)
            break
    ll.appendNode(temphead)
print("After : "+str(ll))

