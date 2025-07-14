import csv
e = [1,'Malhar','Vollyball','Won']


def CREATE():
    file = open("Result.csv","w",newline="")
    writer = csv.writer(file)
    writer.writerow(['St_Id','St_Name','Game_Name','Result'])
    for i in range(int(input("How many records do you want to add: "))):
        writer.writerow(eval(input("Enter a record: ")))
    file.close()

def SEARCH():
    file = open("Result.csv", "r")
    data = csv.reader(file)
    hasWon = False
    winNumber = 0
    for i in list(data)[1:]:
        if i[-1] == "Won":
            winNumber+=1
            hasWon = True
    if hasWon:
        print(winNumber)
    else:
        print("No students have won")

    file.close()

CREATE()
SEARCH()