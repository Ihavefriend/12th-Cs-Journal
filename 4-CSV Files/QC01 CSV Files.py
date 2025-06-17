import csv

def CREATE():
    file = open("TOY.csv","w",newline="")
    writer = csv.writer(file)
    writer.writerow(["NAME","PRICE","CATEGORY","STK"])
    writer.writerows(eval(input("Enter the records")))
    file.close()
CREATE()


def DISPLAY():
    file = open("TOY.csv","r")
    data = list(csv.reader(file))[1:]
    for i in data:
        print(i)
    file.close()


def SEARCH():
    file = open("TOY.csv","r")
    data = csv.reader(file)
    found = False
    target = input("Enter the toy: ")
    for i in data:
        if i[0].lower() == target:
            print(i)
            found = True
    if not found:
        print("Value not found")
    file.close()


def APPEND():
    file = open("TOY.csv","a",newline="")
    writer = csv.writer(file)
    writer.writerows(eval(input("Enter the records to append: ")))
    file.close()


def HIGHEST():
    high = open("HIGHEST.csv","w",newline = "")
    writer = csv.writer(high)
    file = open("TOY.csv","r")
    data = list(csv.reader(file))[1:]
    for i in data:
        if int(i[1]) > 100:
            writer.writerow(i)


def MODIFY():
    file = open("TOY.csv", "r")
    data = list(csv.reader(file))
    file.close()
    for i in range(1, len(data)):
        if int(data[i][3]) < 10:
            data[i][3] = str(int(data[i][3]) + 10)
    file = open("TOY.csv", "w", newline="")
    writer = csv.writer(file)
    writer.writerows(data)
    file.close()


def DELETE():
    file = open("TOY.csv", "r")
    data = list(csv.reader(file))
    new_data = [data[0]]
    isDeleted = False
    for i in range(1, len(data)):
        if data[i][2].lower() != "fun":
            new_data.append(data[i])
        else:
            isDeleted = True
    if isDeleted:
        file = open("TOY.csv", "w", newline="")
        writer = csv.writer(file)
        writer.writerows(new_data)
        file.close()
    file.close()


while True:
    print("\nTOY STORE MANAGEMENT SYSTEM")
    print("1. Display all toys")
    print("2. Search for a toy")
    print("3. Append new toys")
    print("4. Create HIGHEST.CSV (price > 100)")
    print("5. Modify stock (stock < 10)")
    print("6. Delete FUN category toys")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        DISPLAY()
    elif choice == '2':
        SEARCH()
    elif choice == '3':
        APPEND()
    elif choice == '4':
        HIGHEST()
    elif choice == '5':
        MODIFY()
    elif choice == '6':
        DELETE()
    elif choice == '7':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")