import sys
class stack :
    def __init__(self):
        self.data_list=[]
    def push(self,data):
        self.data_list.append(data)
    def pop(self):
        if not self.data_list:
            return -1
        return_data=self.data_list[-1]
        self.data_list=self.data_list[:-1]
        return return_data
    def size(self):
        return len(self.data_list)
    def empty(self):
        if self.data_list:
            return 0
        else:
            return 1
    def top(self):
        if self.data_list:
            return self.data_list[-1]
        else :
            return -1

case_num = int(sys.stdin.readline())
temp_stack = stack()
answer_list=[]
for _ in range(case_num):
    case=sys.stdin.readline().split()
    if case[0]=="push":
        temp_stack.push(int(case[1]))
    elif case[0]=="pop":
        answer_list.append(temp_stack.pop())
    elif case[0]=="size":
        answer_list.append(temp_stack.size())
    elif case[0]=="empty":
        answer_list.append(temp_stack.empty())
    elif case[0]=="top":
        answer_list.append(temp_stack.top())
        
for ans in answer_list:
    print(ans)