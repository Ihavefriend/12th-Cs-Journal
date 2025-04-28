"""
Write a function move() to accept a list of numbers as arguments and put all numbers divisible by 5 to the right.
"""
def move(nums):
    nlist = []
    divb5 = []
    for i in nums:
        if i%5 == 0:
            divb5.append(i)
        else:
            nlist.append(i)
    nlist.extend(divb5)
    return nlist

print(move([1,2,3,4,5,6,10,90,23,30]))