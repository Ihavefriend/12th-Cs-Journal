"""
Write a menu driven program to do the following task with the help of user defined functions :
a) . Check whether the number is even and return true if it is even else return false
b) Check whether number is prime or not
c) Exit
"""
# Defining the functions
def isevenorno():
    n = int(input("Enter the number: "))
    if n%2 == 0:
        return True
    else: return False
def isprime():
    n = int(input("Enter the number: "))
    for i in range(2,n):
        if n%i == 0:
            return False
    else: return True

# Menu Driven Program
while True:
    print("""
1) Check whether the number is even and return true if it is even else return false 
2) Check whether number is prime or not 
3) Exit 
""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(isevenorno())
    if choice == 2:
        print(isprime())
    if choice == 3:
        break