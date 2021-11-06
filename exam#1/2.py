print(' *** Divisible number ***')
num = input('Enter a positive number : ')
num = int(num)
total = 0
if num <= 0:
    print(str(num)+ ' is OUT of range !!!')
else:
    print('Output ==> ',end='')
    for i in range(1,num+1):
        if num%i == 0:
            print(i,end=' ')
            total+=1
    print('')
    print('Total ==>',str(total))