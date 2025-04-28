"""Write a code in Python that counts the number of “The” or “This” words present in a text file “MY_TEXT_FILE.TXT”."""
file = open("MY_TEXT_FILE.txt")
wordslist = file.read().split()
count = {"The":0,"This":0}
for word in wordslist:
    if word in count:
        count[word]+=1
for i in count:
    print(i,":",count[i])
file.close()