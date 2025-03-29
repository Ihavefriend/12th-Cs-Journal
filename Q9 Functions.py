"""
A dictionary called vehicle with the following key:value pairs:
veh={vtype:[brand,model,year,price], vtype:[brand,model,year,price], … }
Write a program to accept the dictionary and counting the number of vehicles released in 2020.
Also display all vehicles in alphabetical order with its brand name.
"""

def vehoperations(veh):
    count2020 = 0
    for i in veh:
        if veh[i][2] == 2020:
            count2020+=1

    print(count2020)
    def brand(x):
        return x[1][0]

    sortedveh = sorted(veh.items(),key=brand)
    print(dict(sortedveh))

veh = {
    "Sedan": ["Toyota", "Camry", 2020, 25000],
    "SUV": ["Ford", "Explorer", 2021, 35000],
    "Truck": ["Chevrolet", "Silverado", 2020, 40000],
    "Hatchback": ["Honda", "Civic", 2019, 22000]
}
vehoperations(veh)

