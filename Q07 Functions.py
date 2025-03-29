"""
Write a program to input two numbers in the main program and write a function findbig() which returns the bigger number.
"""

def findbig(a,b):
    if a>b:
        print(a)
    if b>a:
        print(b)
    if b==a:
        print(f"{a} is equal to {b}")

findbig(int(input("Enter the first number: ")),int(input("Enter the second number: ")))