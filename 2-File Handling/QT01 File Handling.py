"""Write a function in python to count the number lines in a text file ‘Country.txt’ which is starting with an alphabet ‘W’ or ‘H’."""
def countWH():
    with open("Country.txt","r") as file:
        lines = file.readlines()
        count=0
        for line in lines:
            if line[0] in "WH":
                count += 1
    return count
print(countWH())