"""Write a function COUNT_AND( ) in Python to read the text file “STORY.TXT”
and count the number of times “AND” occurs in the file. (include AND/and/And in the counting)"""
def COUNT_AND():
    with open("STORY.txt") as file:
        count = 0
        words = file.read().split()
        for word in words:
            if word in ["AND","and","And"]:
                count+=1
    return count
print(COUNT_AND())