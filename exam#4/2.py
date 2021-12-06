
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class AVL:
    def __init__(self):
        self.root = None

    def insert(self,node,data):
        if node == None:
            return Node(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        if data >= node.data:
            node.right = self.insert(node.right,data)
        balance = self.height(node.left) - self.height(node.right)
        if balance > 1 and data < node.left.data: #left left
            return self.rightRotate(node)
        if balance < -1 and data >= node.right.data: #right right
            return self.leftRotate(node)
        if balance > 1 and data >= node.left.data: #left right
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance < -1 and data < node.right.data: #right left
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        return node

    def height(self,node):
        if node == None:
            return 0
        height_left = self.height(node.left)
        height_right = self.height(node.right)
        if height_left > height_right:
            return height_left + 1
        else:
            return height_right + 1

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        return y
 
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        return y
    
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

print(' *** AVL Tree ***')
T = AVL()
inp = [int(i) for i in input('Enter some numbers : ').split()]
for i in inp:
    T.root = T.insert(T.root,i)

print('in_order  -->', T.in_order(T.root))    
print('preorder  -->', T.pre_order(T.root))
print('postorder -->', T.post_order(T.root))

