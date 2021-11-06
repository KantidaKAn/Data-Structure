def Max (arr,num):
    if len(arr) == 0 :
        return num
    if num < arr[0]:
        num = arr[0]
    arr.pop(0)
    return Max(arr,num)

inp = list(map(int,input('Enter Input : ').split()))
print('Max : '+ str(Max(inp,inp[0]))) 