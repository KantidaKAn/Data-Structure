print(' *** Wind classification ***')
inp = float(input('Enter wind speed (km/h) : '))
if inp < 0 :
    print("!!!Wrong value can't classify.")
else:
    print('Wind classification is ',end='')
    if inp >= 0 and inp < 52 :
        print('Breeze.')
    elif  inp < 56 :
        print('Depression.')
    elif inp < 102 :
        print('Tropical Storm.')
    elif inp < 209 :
        print('Typhoon.')
    else:
        print('Super Typhoon.')