def bubble_sort(lists) :
    
    n = len(lists)
    item = 1
    L = []
    for lasts in range(len(lists) -1,-1,-1) :
        swap = False

        for i in range(lasts):
                if lists[i] > lists[i+1] :
                    lists[i],lists[i+1] = lists[i+1],lists[i]
                    swap = True
        if swap:
            item += 1
            
    count = 0
    for i in range(1,item+1) :      
        compare = n - i 
        count += compare
    print()
    print(lists)
    print("Data comparison =",count)

print(" *** Bubble sort ***")    
input_string = input("Enter some numbers : ")

A=[]
for n in input_string.split():
    A.append(int(n))
bubble_sort(A)