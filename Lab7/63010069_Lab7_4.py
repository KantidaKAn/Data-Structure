'''
Chapter : 7 - item : 4 - สนุกไปกับ Binary Search Tree

ให้น้องรับ input เข้ามาและสร้าง Binary Search Tree ต่อมาให้แสดงผลแบบ Preorder , Inorder , Postorder และ Breadth First Search ตามลำดับ
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

class Binarysearchtree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        node = self.root
        while True:
            if data < node.data:
                if node.left == None:
                    node.left = Node(data)
                    return self.root
                node = node.left
            else:
                if node.right == None:
                    node.right = Node(data)
                    return self.root
                node = node.right
    
    def pre_order(self, node):
        if node == None:
            return ''

        s = str(node.data) + ' '\
            + self.pre_order(node.left)\
                + self.pre_order(node.right)
        return s

    def in_order(self, node):
        if node == None:
            return ''

        s = self.in_order(node.left)\
             + str(node.data) + ' '\
                 + self.in_order(node.right)
        return s

    def post_order(self, node):
        if node == None:
            return ''
        
        s = self.post_order(node.left)\
            + self.post_order(node.right)\
                + str(node.data) + ' '
        return s

    def BFS(self): 
        q = Queue()
        q.enqueue(self.root)
        s = "Breadth : "
        while not q.is_empty():
            node = q.dequeue()
            s += str(node.data) + ' '
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return s

T = Binarysearchtree()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
    
print('Preorder :', T.pre_order(root))
print('Inorder :', T.in_order(root))
print('Postorder :', T.post_order(root))
print(T.BFS())