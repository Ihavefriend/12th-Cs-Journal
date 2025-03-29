"""
Write a function count() which accepts a variable length argument
and counts the number of odd and even numbers and return both the values.
 """

def count(*n):
    count = {"even":0,"odd":0}
    for i in n:
        if i%2 == 0:
            count["even"]+=1
        if i%2 !=0:
            count["odd"]+=1
    return(count["even"],count["odd"])
print(count(1,2,3,4,5))