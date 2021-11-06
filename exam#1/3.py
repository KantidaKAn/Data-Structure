print(' *** String count ***')
Data = input('Enter message : ')
Big = 0
Small = 0
Biglist = []
Smalllist= []
for i in Data :
    if i.isupper() :
        Big += 1
        Biglist.append(i)
    if i.islower():
        Small += 1
        Smalllist.append(i)
Biglist.sort()
Smalllist.sort()
print('No. of Upper case characters : '+str(Big))
if Big > 0 :
    print('Unique Upper case characters : '+str(Biglist[0]),end='  ')
else:
    print('Unique Upper case characters : ',end='')
for i in range(1,len(Biglist)):
    if Biglist[i] != Biglist[i-1]:
        print(Biglist[i],end='  ')
print('')
print('No. of Lower case Characters : '+str(Small))
if Small > 0 :
    print('Unique Lower case characters : '+str(Smalllist[0]),end='  ')
else:
    print('Unique Lower case characters : ',end=(''))
for i in range(1,len(Smalllist)):
    if Smalllist[i] != Smalllist[i-1]:
        print(Smalllist[i],end='  ')
print('')
