import pickle
def CREATE():
    file = open("student.dat", "wb")
    n = int(input("Enter number of records: "))
    for i in range(n):
        roll = int(input("Enter Roll: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        house = input("Enter House: ")
        pickle.dump([roll, name, marks, house], file)
    file.close()
def DISPLAY():
    try:
        file = open("student.dat", "rb")
        while True:
            print(pickle.load(file))
    except EOFError:
        file.close()
def SEARCHNAME():
    target = input("Enter name to search: ")
    file = open("student.dat", "rb")
    found = False
    try:
        while True:
            student = pickle.load(file)
            if student[1].lower() == target.lower():
                print(student)
                found = True
    except EOFError:
        file.close()
    if not found:
        print("Student not found")
def SEARCHID():
    target = int(input("Enter roll to search: "))
    file = open("student.dat", "rb")
    found = False
    try:
        while True:
            student = pickle.load(file)
            if student[0] == target:
                print(student)
                found = True
    except EOFError:
        file.close()
    if not found:
        print("student not found")
def APPEND():
    file = open("student.dat", "ab")
    n = int(input("Enter number of records to append: "))
    for i in range(n):
        roll = int(input("Enter Roll: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        house = input("Enter House: ")
        pickle.dump([roll, name, marks, house], file)
    file.close()
def COUNT():
    file = open("student.dat", "rb")
    total = 0
    sum = 0
    try:
        while True:
            record = pickle.load(file)
            total += 1
            sum += record[2]
    except EOFError:
        file.close()
    print("Total records:", total)
    if total > 0:
        print("Average marks:", sum / total)
def HIGHEST():
    sfile = open("student.dat", "rb")
    tfile = open("high.dat", "wb")
    try:
        while True:
            record = pickle.load(sfile)
            if record[2] > 90:
                pickle.dump(record, tfile)
    except EOFError:
        sfile.close()
        tfile.close()
def MODIFY():
    list = []
    file = open("student.dat", "rb")
    try:
        while True:
            student = pickle.load(file)
            if student[2] < 23:
                student[2] += 10
            list.append(student)
    except EOFError:
        file.close()
    file = open("student.dat", "wb")
    for record in list:
        pickle.dump(record, file)
    file.close()
def DELETE():
    list = []
    file = open("student.dat", "rb")
    try:
        while True:
            student = pickle.load(file)
            if student[3].lower() != "emerald":
                list.append(student)
    except EOFError:
        file.close()
    file = open("student.dat", "wb")
    for record in list:
        pickle.dump(record, file)
    file.close()
def DELETEROLL():
    target = int(input("Enter roll to delete: "))
    list = []
    found = False
    file = open("student.dat", "rb")
    try:
        while True:
            student = pickle.load(file)
            if student[0] == target:
                found = True
            else:
                list.append(student)
    except EOFError:
        file.close()
    if found:
        file = open("student.dat", "wb")
        for record in list:
            pickle.dump(record, file)
        file.close()
        print("Record deleted")
    else:
        print("Record not found")
while True:
    print("\nMenu Options:")
    print("1. Create records")
    print("2. Display records")
    print("3. Search by name")
    print("4. Search by roll")
    print("5. Append records")
    print("6. Count records and average")
    print("7. Create high achievers file")
    print("8. Modify low marks")
    print("9. Delete Emerald house records")
    print("10. Delete by roll")
    print("11. Exit")

    choice = int(input("Enter your choice (1-11): "))

    if choice == 1:
        CREATE()
    elif choice == 2:
        DISPLAY()
    elif choice == 3:
        SEARCHNAME()
    elif choice == 4:
        SEARCHID()
    elif choice == 5:
        APPEND()
    elif choice == 6:
        COUNT()
    elif choice == 7:
        HIGHEST()
    elif choice == 8:
        MODIFY()
    elif choice == 9:
        DELETE()
    elif choice == 10:
        DELETEROLL()
    elif choice == 11:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 11.")
