def Metadrome(inp): 
    for i in range(0,len(inp)):
        for j in range(i+1,len(inp)):
            if inp[i] >= inp[j]:
                return 0
    return 1

def Plaindrome(inp): 
    for i in range(0,len(inp)):
        for j in range(i+1,len(inp)):
            if inp[i] > inp[j]:
                return 0
    return 2

def Katadrome(inp): 
    for i in range(0,len(inp)):
        for j in range(i+1,len(inp)):
            if inp[i] <= inp[j]:
                return 0
    return 3

def Nialpdrome(inp):
    for i in range(0,len(inp)-1):
        for j in range(i+1,len(inp)):
            if inp[i] < inp[j]:
                return 0
    return 4

def Repdrome(inp):
    for i in range(0,len(inp)-1):
        for j in range(i+1,len(inp)):
            if inp[i] == inp[j]:
                c = 1
            else:
                return 0
    if c == 1:  return 5

inp = input("Enter Input : ")
r = Repdrome(inp)
m = Metadrome(inp)
p = Plaindrome(inp)
k = Katadrome(inp)
n = Nialpdrome(inp)

if r == 5:      print("Repdrome")
elif m == 1:    print("Metadrome")
elif p == 2:    print("Plaindrome")
elif k == 3:    print("Katadrome")
elif n == 4:    print("Nialpdrome")
else:           print("Nondrome")