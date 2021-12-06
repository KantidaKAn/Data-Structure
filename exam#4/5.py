count = 0 
def MergeSort(lists):
    if len(lists) > 1 :
        mid = len(lists)//2
        L = lists[:mid]
        R = lists[mid:]
        MergeSort(L)
        MergeSort(R)

        i = 0
        j = 0
        k = 0 
        
        global count
        while i < len(L) and j < len(R) :
            count += 1
            if L[i] < R[j]:
                lists[k] = L[i]
                i += 1
            else :
                lists[k] = R[j]
                j +=1 
            k += 1  
        
        while i < len(L):
            lists[k]= L[i]
            i += 1
            k += 1

        while j < len(R):
            lists[k]= R[j]
            j += 1
            k += 1

def printlist(lists):
    string = ""
    for i in range(len(lists)):
        string += str(lists[i])+" "
    return string

print(" *** Merge sort ***")
lists = list(map(int,input("Enter some numbers : ").split()))
MergeSort(lists)
print()
print("Sorted -> "+printlist(lists))
print("Data comparison =  "+str(count))