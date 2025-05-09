import pickle
def appenddict():
    file = open("employee.dat","ab")
    for i in range(int(input("enter how many employees you want to add: "))):
        pickle.dump(eval(input("enter the dictionary: ")),file)
    file.close()
appenddict()