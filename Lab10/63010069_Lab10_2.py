def min(lx,x):
    for i in lx:
        if x < i:
            return str(i)
    return "No First Greater Value"
inp1,inp2 = input('Enter Input : ').split('/')
lx = [int(i) for i in inp1.split()]
ly = [int(i) for i in inp2.split()]
lx = sorted(lx)
for i in ly:
    print(min(lx,i))