import pickle
def create():
    file = open("employee.dat","wb")
    for i in range(int(input("enter no of employees"))):
        pickle.dump(eval(input("enter the employee")),file)
    file.close()
def Manager():
    try:
        fileR = open("employee.dat","rb")
        mlist = []
        while True:
            i =pickle.load(fileR)
            if i[3].lower() == "manager":
                mlist.append(i)
    except EOFError:
        fileR.close()
        fileW = open("manager.dat","wb")
        for i in mlist:
            pickle.dump(i,fileW)
        fileW.close()
def Accountant():
    try:
        fileR = open("employee.dat","rb")
        alist = []
        while True:
            i =pickle.load(fileR)
            if i[3].lower() == "accountant":
                alist.append(i)
    except EOFError:
        fileR.close()
        fileW = open("accountant.dat","wb")
        for i in alist:
            pickle.dump(i,fileW)
        fileW.close()
create()
Manager()
Accountant()