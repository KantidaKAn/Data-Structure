def bi_search(l, r, arr, x):
    if l==r:
        if arr[l]==x:
            return True
        else :
            return False

    elif l > r:
        return False

    z = arr[(l+r)//2]
    if z > x :
        return bi_search(l, (l+r)//2, arr, x)

    elif z < x :
        return bi_search(((l+r)//2)+1,r , arr, x)

    elif z == x :
        return True
		
    return False

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))