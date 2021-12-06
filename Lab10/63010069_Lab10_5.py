def mw(lis, box): 
    if box == 1:
        return sum(lis)
    minw = sum(lis)+1
    for i in range(len(lis)):
        if len(lis[i:]) < box - 1:
            break
        tb = sum(lis[:i])
        ob = mw(lis[i:], box - 1)
        minw = min(max(tb, ob),minw)
    return minw
x, y = input("Enter Input : ").split('/')
lst = [int(i) for i in x.split()]
print(f'Minimum weigth for {y} box(es) = {mw(lst, int(y))}')