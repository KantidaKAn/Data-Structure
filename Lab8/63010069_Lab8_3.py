n, inp = input("Enter Input : ").split("/")
n = int(n)

inp = inp.split()
inp = list(map(int, inp))

if (n+1)//2 >= len(inp):
    i = 0
    while len(inp) < n:
        inp.insert(0, -111)
        i += 1

    def cal(cur):

        if inp[cur] != -111:
            return

        cal(2*cur+1)
        cal(2*cur+2)

        x = min(inp[2*cur+2], inp[2*cur+1])
        inp[cur] = x
        inp[2*cur+1] -= x
        inp[2*cur+2] -= x


    cal(0)
    print(sum(inp))

else:
    print("Incorrect Input")