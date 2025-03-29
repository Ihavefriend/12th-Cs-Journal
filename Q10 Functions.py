"""
Write a function INDEX_TUPLE(T), where T is the list of tuple elements passed as argument to the function.
The function returns another list named ‘indexList’ that stores the indices of all Non-Zero Elements of T.
"""

def INDEX_TUPLE(T):
    indexlist = []
    for i in range(len(T)):
        if T[i] !=0:
            indexlist.append(i)
    print(indexlist)
INDEX_TUPLE((1,2,0,9,0,8))