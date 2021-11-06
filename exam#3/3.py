import math
def G ( num1, num2) :
    num1 = abs(num1)
    num2 = abs(num2)
    if num2 == 0 :
        return num1
    if num1%num2 == 0 :
        return num2
    else :
        return G(num2, num1%num2)

num1,num2 = map(int,input('Enter Input : ').split())
if num2 < 0 and num1 == 0:
    num1,num2 = num1,num2
elif num1 < 0 and num2 == 0:
    num1,num2 = num2,num1
elif abs(num2) > abs(num1):
    num1,num2 = num2,num1
if num1 == 0 and num2 == 0:
    print('Error! must be not all zero.')
else:
    print(f'The gcd of {num1} and { num2 } is : {str(G(num1,num2))}')   