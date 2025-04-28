"""Write a method/function ISTOUPCOUNT() in python to read contents from a text file WRITER.TXT,
to count and display the occurrence of the word ‘‘IS’’ or ‘‘TO’’ or ‘‘UP’’"""
def ISTOUPCOUNT():
    file = open("WRITER.txt")
    words = file.read().lower().split()
    count = {"is":0,"to":0,"up":0}
    for word in words:
        if word in count:
            count[word] +=1
    file.close()
    return count
dict = ISTOUPCOUNT()
for i in dict:
    print(i,":",dict[i])