"""Write a function in python that displays the number of lines starting with ‘H’ in the file “para.txt”."""
def countH():
    with open("Diary.txt","r") as file:
        count = 0
        lines = file.readlines()
        for line in lines:
            if line[0] in "Hh":
                count+=1
    return count
print(countH())