"""Write a user defined function countwords() to display the total number of words present in the file from a text file “Quotes.Txt”"""
def countwords():
    file = open("Country.txt","r")
    words = file.read()
    wordlist = words.split()
    wordcount = len(wordlist)
    file.close()
    return wordcount
print(countwords())