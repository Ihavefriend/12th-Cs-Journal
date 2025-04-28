"""Write a function in python to read lines from file “POEM.txt” and display all those words, which has two characters in it."""
def twowords():
    with open("POEM.txt","r") as file:
        words = file.read().split()
        for word in words:
            if len(word) == 2:
                print(word)
twowords()