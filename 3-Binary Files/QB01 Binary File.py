import pickle
def createb():
    file = open("employee.dat","wb")
    n = int(input(('enter how many employee details you wish to enter: ')))
    for i in range(n):
        e = eval(input("enter the dictionary: "))
        pickle.dump(e,file)
    print("Your file has been created.")
    file.close()
def search():
    try:
        file = open("employee.dat","rb")
        empfound = False
        L=[]
        target = int(input("enter the target employee number"))
        while True:
            emp = pickle.load(file)
            if emp["employeeno"] == target:
                empfound = True
                if emp["salary"] < 20000:
                    emp["salary"] += 2000
                    print(emp)
                    L.append(emp)
    except EOFError:
        file.close()
        file = open("employee.dat","wb")
        if not empfound:
            print("Employee number not found in given data")
        for i in L:
            pickle.dump(i,file)
search()