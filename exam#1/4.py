print('*** String Rotation ***')

a,b = map(list,input('Enter 2 strings : ').split())

A = a.copy()
B = b.copy()

round = 0 
while(A != a or B != b)or round < 1:
    A = A[-1:] + A[:len(a)-1]
    B = B[1:] + B[:1]

    round+=1
    if round < 6 or( A == a and B == b ):
        print(f'{round} {"".join(A)} {"".join(B)}')
    elif round == 6:
        print(' . . . . . ')
print(f'Total of  {round} rounds.')