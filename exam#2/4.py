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

print(' *** Re order ***')
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