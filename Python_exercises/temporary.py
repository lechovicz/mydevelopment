class Vehicle():
    cars = []

    def __init__(self, name, kind, color, value):

        self.name = name
        self.kind = kind
        self.color = color
        self.value = value
        self.cars.append(name)

    def descript(self):
        print "%s is a %s, %s worth %d" % (self.name, self.color, self.kind, self.value)



car1 = Vehicle('doggy', 'hatch', 'blue', 10000)
car1.descript()
car2 = Vehicle('karo','truck', 'red', 666)
car2.descript()

print "Vehicles in the databases are: "
for x in Vehicle.cars:
    print x