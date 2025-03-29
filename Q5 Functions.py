"""
Write a Python function that finds and displays all the words longer than 5 characters from the input given by the user.
"""

def isitlongerthanfivecharacters():
    wordslongerthan5characters = []
    sentence = input("Enter the sentence: ")
    for i in sentence.split():
        if len(i)>5:
            wordslongerthan5characters.append(i)
    print(wordslongerthan5characters)
isitlongerthanfivecharacters()