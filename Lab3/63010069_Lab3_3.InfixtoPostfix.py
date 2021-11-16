'''
Chapter : 3 - item : 3 - Infix to Postfix

ให้รับ Input เป็น  Infix  และแสดงผลลัพธ์ออกมาเป็น Postfix โดยจะมี Operator  5  แบบ  ได้แก่  +   -   *   /   ^

'''

class Stack():
    def __init__(self, ls = None):
        if ls == None:
            self.items = []
        else:
            self.items = list()     

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def viwe(self):
        return self.items[-1]

def infix2postfix(exp) :

    s = Stack()
    postfix = ""
    # print(s.items)
    
    for i in exp:
        # print(s.items , postfix)
        if i.isalpha() == True:
            postfix += i
        elif i == "(":
            s.push(i)
        elif i == ")":          
            while s.viwe() != "(":
                postfix += s.pop() 
            s.pop()
        elif i in ("+-*/"):
            if s.isEmpty():
                s.push(i)
            else:
                if (i in ("*","/") and s.viwe() in ("+","-") )or s.viwe() == "(":
                    s.push(i)
                else:
                    if i in ("+-"):
                        while s.viwe() != "(" :
                            postfix += s.pop()
                            if s.isEmpty():
                                break
                    else:
                        while s.viwe() not in ("(+-") :
                            postfix += s.pop()
                            if s.isEmpty():
                                break
                    s.push(i)
        elif i == "^" :
            if s.isEmpty():
                s.push(i)
            elif s.viwe() != "^":
                s.push(i)
            else:
                 while s.viwe() != "^" :
                            postfix += s.pop()
                            if s.isEmpty():
                                break




    while not s.isEmpty():
        postfix += s.pop()


    return postfix
        

#print("***Infix to Postfix*** ")

inp = input("Enter Infix : ")

print("Postfix : ",end="")

print(infix2postfix(inp))
