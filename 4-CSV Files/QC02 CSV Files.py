import csv

def CREATE():
    file = open("student.csv","w",newline="")
    writer = csv.writer(file)
    for i in range(int(input("How many students records do you want to add: "))):
        writer.writerow(eval(input("Enter one students record: ")))
    file.close()


def DISPLAY():
    file = open("student.csv","r")
    data = csv.reader(file)
    for i in data:
        print(i)
    file.close()


def SEARCH():
    file = open("student.csv", "r")
    data = csv.reader(file)
    isFound = False
    target = input("Enter the students name: ")
    for i in data:
        if i[0].lower() == target:
            print(i)
            isFound = True
    if not isFound:
        print("Value not found")
    file.close()

def APPEND():
    file = open("student.csv","a",newline="")
    writer = csv.writer(file)
    writer.writerow(eval(input("Enter the records to append: ")))
    file.close()


def FAILURE():
    fail = open("FAILURE.csv","w",newline = "")
    writer = csv.writer(fail)
    file = open("student.csv","r")
    data = list(csv.reader(file))
    for i in data:
        print(i)
        for j in range(1,6):
            print(int(i[j]))
            if int(i[j]) < 33:
                writer.writerow(i)
    fail.close()
    file.close()


def MODIFY():
    file = open("student.csv", "r")
    data = list(csv.reader(file))
    file.close()
    for i in range(1, len(data)):
        if int(data[i][2]) < 50:
            data[i][2] = str(int(data[i][2]) + 10)
    file = open("student.csv", "w", newline="")
    writer = csv.writer(file)
    writer.writerows(data)
    file.close()


def DELETE():
    file = open("student.csv", "r")
    data = list(csv.reader(file))
    file.close()
    new_data = []
    isDeleted = False
    for i in data:
        avg = (int(i[1])+int(i[2])+int(i[3])+int(i[4])+int(i[5]))/5
        if avg >= 40:
            new_data.append(i)
        else:
            isDeleted = True
    if isDeleted:
        file = open("student.csv", "w", newline="")
        writer = csv.writer(file)
        writer.writerows(new_data)
        file.close()
    file.close()


while True:
    print("\n===== Student Records Menu =====")
    print("1. CREATE student.csv")
    print("2. DISPLAY contents of student.csv")
    print("3. SEARCH by name")
    print("4. APPEND records")
    print("5. FAILURE list to fail.txt")
    print("6. MODIFY CS marks")
    print("7. DELETE students")
    print("8. EXIT")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        CREATE()
    elif choice == '2':
        DISPLAY()
    elif choice == '3':
        SEARCH()
    elif choice == '4':
        APPEND()
    elif choice == '5':
        FAILURE()
    elif choice == '6':
        MODIFY()
    elif choice == '7':
        DELETE()
    elif choice == '8':
        print("Exiting the program.")
        break

