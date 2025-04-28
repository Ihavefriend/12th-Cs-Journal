"""
A dictionary called vehicle with the following key:value pairs:
veh={vtype:[brand,model,year,price], vtype:[brand,model,year,price], … }
Write a program to accept the dictionary and counting the number of vehicles released in 2020.
Also display all vehicles in alphabetical order with its brand name.
"""

def sortbrand(veh):
    veh_items = list(veh.items())
    for i in range(len(veh_items)):
        for j in range(i + 1, len(veh_items)):
            if veh_items[i][1][0] > veh_items[j][1][0]:
                veh_items[i], veh_items[j] = veh_items[j], veh_items[i]

    print(dict(veh_items))

def vehoperations(veh):
    count2020 = 0
    for i in veh:
        if veh[i][2] == 2020:
            count2020+=1

    print(count2020)

veh = {
    "Sedan": ["Toyota", "Camry", 2020, 25000],
    "SUV": ["Ford", "Explorer", 2021, 35000],
    "Truck": ["Chevrolet", "Silverado", 2020, 40000],
    "Hatchback": ["Honda", "Civic", 2019, 22000]
}
vehoperations(veh)
sortbrand(veh)