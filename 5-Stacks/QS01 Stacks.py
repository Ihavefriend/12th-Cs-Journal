train = []
top = None

def push(stk,item):
    global top
    if type(item) == type((1,)):
        stk.append(item)
        top = len(stk)-1
    else:
        print("Enter a Tuple")

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
            print(stk[i])

while True:
    print("""   ~~~~~~~~~~~~~~~~~~~
    1. Push an element 
    2. Pop an element
    3. Peek the stack
    4. Display the stack
    5. Exit
    ~~~~~~~~~~~~~~~~~~""")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        push(train,eval(input("Enter the Tuple")))
    if choice == 2:
        print(pop(train))
    if choice == 3:
        print(peek(train))
    if choice == 4:
        print(display(train))
    if choice == 5:
        break