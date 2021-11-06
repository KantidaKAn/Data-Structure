class Queue:
    def __init__(self,L=None) :
        if L == []:
            self.item =[]
        else :
            self.item = L
    def __str__ (self) :
        if len(self.item) == 0 :
            return 'Empty Queue'
        s ='Queue data : '
        for i in self.item:
            s += str(i) + ' '
        return s
    def __len__(self):
        return len(self.item)
    def enQueue(self,data):
        self.item.append(data)
    def  deQueue(self):
        return self.item.pop(0)
    def isEmpty(self):
        return self.item == []
    def checkD(self):
        temp = self.item
        temp.sort()
        for i in range (len(temp)-1):
            if temp[i]==temp[i+1]:
                return True 
        return False


left,right = input('Enter Input : ').split('/')
book = left.split(' ')
Q = Queue(book)
command = right.split(',')
for i in command:
    c = i.split(' ')
    if c[0] == 'E' :
        Q.enQueue(c[1])
    elif c[0] == 'D' :
        Q.deQueue()
if Q.checkD()==True:
    print('Duplicate')
else :
    print('NO Duplicate')
