class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root==None:
            self.root = Node(data)
            print('*')
        else :
            intree = False
            item = self.root
            while(not intree) :
                if item.data<=data:
                    if item.right==None:
                        item.right = Node(data)
                        print('R*')
                        break
                    else :
                        print('R',end='')
                        item = item.right
                elif item.data>data:
                    if item.left==None:
                        item.left = Node(data)
                        print('L*')
                        break
                    else :
                        print('L',end='')
                        item = item.left
        return self.root        
    def printtree(self, node, level = 0):
        if node != None:
            self.printtree(node.right, level + 1)
            print('     ' * level, node)
            self.printtree(node.left, level + 1)
T = BinarySearchTree()
inp = [int(x) for x in input('Enter Input : ').split()]
for x in inp:
    root = T.insert(x)