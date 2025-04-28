"""Write a function COUNT() in Python to read contents from file “REPEATED.TXT”, to count and display the occurrence of the word “Catholic” or “mother”."""
def COUNT():
    with open("REPEATED.txt","r") as file:
        count = {"catholic":0,"mother":0}
        words = file.read().lower().split()
        for word in words:
            if word in count:
                count[word] += 1
    return count
dict = COUNT()
for i in dict:
    print(i,":",dict[i])