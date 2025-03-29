"""
Write a Python function that displays all the words containing @cmail from the input given by the user
"""

def findcmail():
    cmailwords = []
    string = input("Enter the sentence: ")
    words = string.split()
    for i in words:
        if "@cmail" in i:
            cmailwords.append(i)
    print(cmailwords)

findcmail()