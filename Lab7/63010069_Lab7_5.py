'''
Chapter : 7 - item : 5 - Expression Tree

ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น Expression Tree , Infix และ Prefix  โดย Operator จะมีแค่ + - * /

'''
class Node():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.right = right
        self.left = left
    
    def __str__(self):
        return str(self.data)

class Binarysearchtree():
    def __init__(self):
        self.root = None
    
    def insertWithPostfix(self, data):
        List = []
        for x in data:
            if x in '+-*/':
                op1 = List.pop(-1)
                op2 = List.pop(-1)
                List.append(Node(x, op1, op2))
            else:
                List.append(Node(x))
        self.root = List.pop()
        return self.root

    def printTree(self, node, level = 0):
        if node:
            self.printTree(node.left, level+1)
            print('     ' * level, node)
            self.printTree(node.right, level+1)

    def printInfix(self, node):
        if node:
            if node.left and node.right:
                print('(', end='')
            self.printInfix(node.right)
            print(node, end='')
            self.printInfix(node.left)
            if node.left and node.right:
                print(')', end='')

    def printPrefix(self, node):
        if node:
            print(node, end='')
            self.printPrefix(node.right)
            self.printPrefix(node.left)

Tree = Binarysearchtree()
inp = input("Enter Postfix : ")
root = Tree.insertWithPostfix(inp)
print('Tree : ');Tree.printTree(root, 0)
print('--------------------------------------------------')
print('Infix : ',end='');Tree.printInfix(root);print()
print('Prefix : ',end='');Tree.printPrefix(root);print()