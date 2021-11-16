'''
Chapter : 2 - item : 3 - Odd And Even
ให้นักศึกษาเขียนโปรแกรมภาษา Python โดยใช้ Function ในการหาตำแหน่ง คู่ กับ คี่ จาก List และ String

def odd_even(arr, s):
    //Code Here

โดยที่รูปแบบการรับ Input ตำแหน่งแรกจะเป็นตัวบอกว่าเป็น String หรือ List ถ้าใส่ S = String ถ้าใส่ L = List

Input ตำแหน่งที่สองเป็นค่าใน String หรือ List ที่นำเข้ามา

Input ตำแหน่งที่สามเป็นการบอกว่าจะแสดงตำแหน่งคู่หรือคี่ ถ้าใส่ Odd = คี่ ถ้าใส่ Even = คู่

'''

def odd_even(Str):
    listAns = []

    if Str[1][1] != ' ' and Str[0] == 'L' and Str[2] == 'Even':
        return print("[]")
    elif Str[1][1] != ' ' and Str[0] == 'L' and Str[2] == 'Odd' :
        return print("['"+Str[1]+"']")

    newList = [ele for ele in Str[1] if ele.strip()]
    for i in range(len(newList)):
        if Str[2] == 'Odd':
            if i % 2 == 0:
                listAns.append(newList[i])
        else:
            if i % 2 != 0:
                listAns.append(newList[i])
    if Str[0] == 'S':
        strAns = ' '.join(map(str,listAns))
        return print(strAns.replace(" ", ""))
    else: 
        print(listAns)
print("*** Odd Even ***") 
inStr = input("Enter Input : ").split(',')
odd_even(inStr)