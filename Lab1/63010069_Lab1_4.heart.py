'''

Chapter : 1 - item : 4 - สนุกไปกับการวาดรูป(1)
เขียนภาษา Python เพื่อวาดรูปหัวใจ ซึ่งจะรับ input เป็นขนาดของรูปหัวใจ โดย input จะมีค่าตั้งแต่ 2 ขึ้นไป

'''

print("*** Fun with Drawing ***")
print("Enter input : ",end="")
lines = int(input()) #จำนวนเเถว
downline = 2 * lines - 2
downc = (downline*2) - 1 #ด้านในหัวใจ
mid = downline*2 + 1
ptA = 1
ptB = 1
tryag1 = 1
tryag2 = 1
leftpt = midpt = rightpt = lines - 1 #จุดตรงกลาง&ซ้าย&ขวา

for i in range(lines-1, 0, -1):
    for j in range(0, leftpt):
        print(end=".")
    leftpt -= 1

    for j in range(0, tryag1):
        if j == 0 or j == tryag1-1:
          print("*",end="")
        else:
          print("+",end="")
    tryag1 += 2

    for j in range(0, midpt*2-1):
        print(end=".")
    midpt -= 1

    for j in range(0, tryag2):
        if j == 0 or j == tryag2-1:
          print("*",end="")
        else:
          print("+",end="")
    tryag2 += 2

    for j in range(0, rightpt):
        print(end=".")
    rightpt -= 1

    print("")

for i in range(0, mid):
    if i == 0 or i == mid-1 or i == mid//2:
     print("*", end='')
    else:
     print("+", end='')

print("")

for i in range(downline, 0, -1):
    for j in range(0, ptA):
        print(end=".")
    ptA += 1

    for j in range(0, downc):
        if j == 0 or j == downc-1:
         print("*",end="")
        else:
         print("+",end="")
    downc-=2

    for j in range(0, ptB):
        print(".",end="")
    ptB += 1

    print("")