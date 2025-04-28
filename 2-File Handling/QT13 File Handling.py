def CREATE():
    file = open("POETIC.txt","a")
    file.close()
def DISPLAY():
    file = open("POETIC.txt","r")
    print(file.read())
    file.close()
def COUNTCHAR():
    file = open("POETIC.txt", "r")
    count = {"vowel":0,"consonant":0,"uppercase":0,"lowercase":0}
    for i in file.read():
        if i.islower():
            count["lowercase"] +=1
        if i.isupper():
            count["uppercase"]+=1
        if i.lower() in "aeiou":
            count["vowel"] +=1
        if i.lower() in "qwrtyplkjhgfdszxcvbnm":
            count["consonant"] +=1
    print(count)
    file.close()
def HASHSHOW():
    with open("POETIC.txt") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                print(word, end="#")
            print()
def COPY():
    old = open("POETIC.txt")
    new = open("special.txt","w")
    wordlist = old.readlines()
    for i in wordlist:
        if "#" in i:
            new.write(i)
    old.close()
    new.close()
def REPLACE():
    file = open("POETIC.txt")
    words = file.read()

    file2 = open("duplicate.txt","w+")

    target = input("Enter the word to be replaced: ")
    replacing = input("Enter the new word: ")
    newwords = words.replace(target, replacing)

    file2.write(newwords)
    file2.flush()
    print("Original Text:")
    print(words)

    file2.seek(0)
    print()
    print("New Text:")
    print(file2.read())
    file.close()
    file2.close()
def DELETE():
    with open("POETIC.txt", "r") as file:
        lines = file.readlines()

    todelete = input("Enter the word to delete: ").strip()

    new_lines = []
    for line in lines:
        words = line.split()
        filwords = []
        for word in words:
            if word != todelete:
                filwords.append(word)
        new_line = " ".join(filwords) + "\n"
        new_lines.append(new_line)

    with open("POETIC.txt", "w") as file:
        file.writelines(new_lines)

def COUNTEND():
    countend = 0
    file = open("POETIC.txt", "r")
    lines = file.readlines()
    for line in lines:
        if line.strip("\n")[-1].lower() in "yi":
            countend+=1
    print(countend)
    file.close()
def VOWEL():
    vowelstart = []
    file = open("POETIC.txt", "r")
    file2 = open("vowels.txt","w+")
    words = file.read()
    word = words.split()
    for i in word:
        if i[0].lower() in "aeiou":
            vowelstart.append(i)
    file2.write("\n".join(vowelstart))
    file2.flush()

    print("Original Text:")
    print(words)

    file2.seek(0)

    print("New Text:")
    print(file2.read())

    file.close()
    file2.close()
def CHANGE():
    file = open("POETIC.txt")
    words = file.read().split()

    file2 = open("POETICchange.txt","w+")
    file2.write("**".join(words))

    file2.flush()
    file2.seek(0)

    print("Original Text:")
    print(" ".join(words))

    file2.seek(0)

    print("New Text:")
    print(file2.read())

    file.close()
    file2.close()


while True:
    print("""What would you like to do?
(1) -> CREATE(): Creates "POETIC.txt"
(2) -> DISPLAY(): Displays the complete content of the file.
(3) -> COUNTCHAR(): Reads the text file and displays the number of vowels, consonants, uppercase, and lowercase characters.
(4) -> HASHSHOW(): Reads the text file line by line and displays each word separated by "#".
(5) -> COPY(): Copies all the lines which contain "#" to another file called "special.txt".
(6) -> REPLACE(): Replaces a word with another user-given word into another file called duplicate.txt. Displays both files.
(7) -> DELETE(): Deletes a given word in the text file.
(8) -> COUNTEND(): Counts the number of lines ending with "y" or "i".
(9) -> VOWEL(): Copies all words that start with a vowel to another file "vowel.txt". Displays both files.
(10) -> CHANGE(): Replaces every space with "**". Displays both files.
(0) -> EXIT""")

    o = int(input("Enter an option: "))
    print()

    if o == 1:
        CREATE()

    elif o == 2:
        DISPLAY()

    elif o == 3:
        COUNTCHAR()

    elif o == 4:
        HASHSHOW()

    elif o == 5:
        COPY()

    elif o == 6:
        REPLACE()

    elif o == 7:
        DELETE()

    elif o == 8:
        COUNTEND()

    elif o == 9:
        VOWEL()

    elif o == 10:
        CHANGE()

    elif o==0:
        break
    else:
        print("Invalid option.")