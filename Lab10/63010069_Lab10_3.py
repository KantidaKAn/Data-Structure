class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, ts,mc):
        self.table = []
        self.mc = mc
        for i in range(ts):
            self.table.append(None)
        self.count = 0
    def printtable(self):
        for i in range(len(self.table)):
            print(f'#{i+1}	{self.table[i]}')
        print('---------------------------')
    def ins(self,data):
        if self.count>len(self.table):
            return
        elif self.count==len(self.table):
            print("This table is full !!!!!!")
            self.count +=1
            return 
        k,v = data.split(' ')
        sumAscii = 0
        for i in k:
            sumAscii+=ord(i)
        sm = sumAscii%len(self.table)
        if self.table[sm]==None:
            if self.count<len(self.table):
                self.table[sm] = Data(k,v)
                self.count+=1
        else :
            print(f'collision number 1 at {sm}')
            isin = False
            for i in range(1,self.mc):
                if self.table[(sm+(i*i))%len(self.table)] ==None:
                    if self.count<len(self.table):
                        self.table[(sm+(i*i))%len(self.table)] = Data(k,v)
                        isin = True
                        self.count+=1  
                        
                        break
                print(f'collision number {i+1} at {(sm+(i*i))%len(self.table)}')
            if not isin:
                print('Max of collisionChain')
        T.printtable()

print(' ***** Fun with hashing *****')
tab,date = input('Enter Input : ').split('/')
lis = [i for i in date.split(',')]
ts,mc = [int(i) for i in tab.split(' ')]
T = hash(ts,mc)
for i in lis:
    T.ins(i)