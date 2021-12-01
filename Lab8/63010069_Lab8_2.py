'''
ให้น้องๆสร้าง AVL Tree ด้วย Class โดยผลลัพธ์ให้แสดงเป็น Tree ในแต่ละรอบหลังจาก Insert ให้ตรวจสอบว่า balance หรือยัง หากไม่ให้ ปรับ Balance ให้เรียบร้อยแล้วและแสดงผล

** ถ้าสงสัยสามารถดู visualization ของ AVL ได้ที่ website นี้ : https://www.cs.usfca.edu/~galles/visualization/AVLtree.html

#code เป็นเพียงตัวอย่างเท่านั้นสามารถเขียนขึ้นเองโดยไม่ต้องอ้างอิงจาก code นี้ก็ได้
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

class AVL:

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def insert(self, root, data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.getHeight(root.right), self.getHeight(root.left))
        balance = self.getBalance(root)

        # Left Left 
        if balance > 1 and data < root.left.data:
            print('Not Balance, Rebalance!') 
            return self.rightR(root) 
        # Right Right 
        if balance < -1 and data >= root.right.data:
            print('Not Balance, Rebalance!') 
            return self.leftR(root) 

        # Left Right 
        if balance > 1 and data >= root.left.data:
            print('Not Balance, Rebalance!') 
            root.left = self.leftR(root.left) 
            return self.rightR(root) 

        # Right Left 
        if balance < -1 and data < root.right.data:
            print('Not Balance, Rebalance!') 
            root.right = self.rightR(root.right) 
            return self.leftR(root) 

        return root

    def leftR(self, z): 
        y = z.right 
        temp = y.left 
        y.left = z 
        z.right = temp
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 
        return y 

    def rightR(self, z): 
        y = z.left 
        temp = y.right 
        y.right = z 
        z.left = temp 
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 
        return y 

    def getHeight(self, root): 
        if not root: 
            return 0
        return root.height 

    def getBalance(self, root): 
        if not root: 
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right) 


inp = list(map(int, input("Enter Input : ").split()))
Tree = AVL()
root = None
for x in inp:
    print("insert :", x )
    root = Tree.insert(root, x)
    Tree.printTree(root)
    print('===============')