count = 0 
def shellsort(lists):
        gap = len(lists) // 2 
    
        while gap > 0 :
            i = 0
            j = gap
            
            while j < len(lists):
        
                if lists[i] > lists[j]:
                    lists[i],lists[j] = lists[j],lists[i]
                
                i += 1
                j += 1
            
                k = i
                while k - gap > -1:
    
                    if lists[k - gap] > lists[k]:
                        lists[k-gap],lists[k] = lists[k],lists[k-gap]
                    k -= 1
    
            gap //= 2
            L = lists[:gap]
            R = lists[gap:]
            shellsort(L)
            shellsort(R)

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

print(" *** Shell sort ***")
lists = list(map(int,input("Enter some numbers : ").split()))
shellsort(lists)
print()
print("Sorted -> "+printlist(lists))
print("Data comparison =  "+str(count))