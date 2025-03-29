"""
Write a program to input a number in the main program and write a
function fact() which find the factorial of the number and prints the answer in the main program.
"""

def fact(n):
    factorial = 1
    for i in range(1,n+1):
        factorial*=i
    print(factorial)

fact(int(input("Enter the number: ")))