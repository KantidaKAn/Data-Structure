inp = [int(i) for i in input('Enter Input : ').split()]
x , y = 0 , 0 

for i in range(len(inp)-1,0,-1):
    for j in range(i):
        if inp[j] > x :
            x = inp[j]
            y = j
    if x > inp[i]:
        inp[y],inp[i] = inp[i],x 
        print(f'swap {inp[y]} <-> {inp[i]} : {inp}')
    x=0
print(inp)