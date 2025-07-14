dict = {49087:'Aarav',56047:'Aayan',38495:'Abbas',27395:'Lalit'}
stack = []


def push(stk,dict):
    global top
    for i in dict:
        if dict[i][0] == "A":
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

push(stack,dict)
display(stack)