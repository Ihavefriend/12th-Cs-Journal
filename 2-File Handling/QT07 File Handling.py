"""Write a method in python to read lines from a text file DIARY.TXT and display those lines which start with the alphabet P."""
def disP():
    with open("Diary.txt","r") as file:
        lines = file.readlines()
        for line in lines:
            if line[0] in "pP":
                print(line,end = "")
disP()