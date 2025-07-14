list = [1,2,3,4,5,6,7,8,9,10]
stack = []

def push(stk,list):
    global top
    for i in list:
        if i%2 == 0:
            stk.append(i)
        top = len(stk)-1

def pop(stk):
    global top
    if len(stk) == 0:
        return "Underflow"
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk) - 1
        return item

def peek(stk):
    global top
    if len(stk) == 0:
        return "Underflow"
    else:
        top = len(stk) - 1
        return stk[top]

def display(stk):
    global top
    if len(stk) == 0:
        return "Stack Empty"
    else:
        top = len(stk) - 1
        for i in range(top,-1,-1):
            print(stk[i],end=" ")

push(stack,list)
display(stack)

