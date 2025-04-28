"""Write a function VowelCount() in Python, which should read each character of a text file MY_TEXT_FILE.TXT,
should count and display the occurrence of alphabets vowels."""
def VowelCount():
    file = open("MY_TEXT_FILE.txt")
    wordslist = file.read().lower().split()
    file.close()
    vowelcount = {"a":0,"e":0,"i":0,"o":0,"u":0}
    for word in wordslist:
        for character in word:
            if character in "aeiou":
                vowelcount[character]+=1
    for vowel in vowelcount:
        print(vowel,":",vowelcount[vowel])
    file.close()
VowelCount()