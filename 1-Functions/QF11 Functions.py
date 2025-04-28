"""
Write a function, vowelCount() in Python that counts and displays the
number of vowels present in the input given by the user as a string.
"""

def vowelCount():
    string = input("Enter the string: ")
    vowlcount = 0
    for i in string.lower():
        if i in "aeiou":
            vowlcount+=1
    print(vowlcount)
vowelCount()