'''
Chapter : 4 - item : 3 - code with queue

รับ string มาเข้าคิวหา secret code โดยรับ input คือ

code เป็น string ยาว

hint คือตัวแรกของรหัสที่ถูกต้อง

**คำใบ้**

ascii ของ "f" มีค่า = 102

ascii ของ "g" มีค่า = 103

ascii ของ "h" มีค่า = 104

ascii ของ "i" มีค่า = 105

ascii ของ "j" มีค่า = 106

'''

class Queue :
    def __init__(self) :
        self.items = []

    def enqueue(self, value) :
        self.items.append(value)

    def dequeue(self) :
        if not self.isEmpty() :
            return self.items.pop(0)
        return -1

    def isEmpty(self) :
        return self.size() == 0

    def size(self) :
        return len(self.items)
        
    def getQueue(self) :
        return self.items

q = Queue()
code,hint = input("Enter code,hint : ").split(",")
for i in range(len(code)):
    q.enqueue(chr(ord(code[i])-(ord(code[0])-ord(hint))))
    print(q.getQueue())