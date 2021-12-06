def bubble_sort(our_list):
    for i in range(len(our_list)):
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]

inp = list(map(int,input("Enter Input : ").split()))
bubble_sort(inp)
print(inp)
