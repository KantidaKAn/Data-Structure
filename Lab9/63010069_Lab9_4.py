inp = input("Enter Input : ").split()
SBAL  = []
for x in inp:
    for y in x:
        if y.isalpha():
            SBAL.append([y,x])
            break
for x in range(len(SBAL)):
    changed = False
    for y in range(0,len(SBAL)-x-1):
        if ord(SBAL[y][0]) > ord(SBAL[y+1][0]):
            SBAL[y],SBAL[y+1] = SBAL[y+1],SBAL[y]
            changed = True
    if changed == False:
        break
for x in SBAL:
    print(x[1],end=" ")