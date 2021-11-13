'''
Chapter : 1 - item : 5 - Countdown มหาสนุก
 
อยากให้นักศึกษาช่วยหาลำดับการ Countdown จาก Input ที่รับเข้ามา โดยลำดับการ Countdown จะเป็นเลขเรียงลำดับ เช่น 2->1 , 3->2->1 โดยจะสิ้นสุดด้วย 1 เสมอ
โดยผลลัพธ์ให้แสดง List ของ จำนวนลำดับที่เจอ และ แต่ละลำดับเป็นอย่างไร

'''

N = []
T = []
def check(x):
    if num[x] == 1 :
        T.append(int(num[x]))
        temp = T.copy()
        N.append(temp)
        n = T[0]
        T.clear()
        return n
    else :
        if x+1< len(num):
            if num[x]-1 == num[x+1]:
                T.append(int(num[x]))
                return check(x+1)
            else :
                T.append(int(num[x]))
                temp = T.copy()

                n = temp[0]-temp[len(temp)-1]+1
                T.clear()
                return n
        else :
            return 1

print("*** Fun with countdown ***")
num = [int(i) for i in input("Enter List : ").split()]

Start = 0
while(Start<len(num)) :
    Start+=check(Start)
print(f'[{len(N)}, {N}]')