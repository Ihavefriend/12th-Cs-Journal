"""
Write a function series() which accepts two values (x and n as arguments) and finds
the sum of the series 1 + x + x2+ x3 +……+ xn and prints the answer in the main program
"""

def series(x,n):
    sum = 0
    for i in range(n):
        sum+=x**i
    sum+= x**n
    print(sum)
series(2,3)