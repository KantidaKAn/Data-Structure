X, Y = input('Enter Input : ').split('/')

X = [int(i) for i in X.split()]
Y = [str(i) for i in Y.split(',')]

sumList = []


def recursion(n):
    sum = 0                             

    if n >= len(X):            
        return 0

    sum += recursion(2 * n + 1)    
    sum += recursion(2 * n + 2)     
    return X[n] + sum          


print(recursion(0))                

for i in Y:
    i = list(map(int, i.split()))      
    sum1 = recursion(i[0])          
    sum2 = recursion(i[1])         

    if sum1 > sum2:
        print(i[0], '>', i[1], sep='')
    elif sum1 < sum2:
        print(i[0], '<', i[1], sep='')
    else:
        print(i[0], '=', i[1], sep='')