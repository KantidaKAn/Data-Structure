def printTree(n, level=0):
    if n > len(num)-1:
        return
    printTree(2 * n + 2, level + 1)
    print('        ' * level, num[n])
    printTree(2 * n + 1, level + 1)


k, List = input('Enter Input : ').split('/')
List = [int(i) for i in List.split()]

num = []
van = {}

for i in range(int(k)):
    num.append(i + 1)   
    van[i+1] = van.get(i+1, 0) 

for i in range(len(List)):

    Minnum = num.pop(0)
    van[Minnum] = van.get(Minnum, 0) + int(List[i])
    print(f'Customer {i+1} Booking Van {Minnum} | {List[i]} day(s)')

    for i in range(len(num)): 

        if van[Minnum] < van[num[i]] or (van[Minnum] == van[num[i]] and Minnum < num[i]):
            num.insert(i, Minnum)  
            Minnum = None
            break

    if Minnum is not None:  
        num.append(Minnum)  