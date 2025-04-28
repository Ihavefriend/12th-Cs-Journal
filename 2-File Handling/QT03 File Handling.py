"""Write a function filter(oldfile, newfile) that copies all the lines of a text file “source.txt”
onto “target.txt” except those lines which starts with “@” sign."""
def filter(oldfile,newfile):
    old = open(oldfile,"r")
    new = open(newfile,"w")
    oldlines = old.readlines()
    for line in oldlines:
        if line[0] != "@":
            new.write(line)
    new.close()
    old.close()
filter("source.txt","target.txt")