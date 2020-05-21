# class Sample():
    # pass
    
# ob = Sample()

# print(ob)

# class Animal():
    # planet = "earth"
    
    # def __init__(self, type, num):
      # self.type = type
      # self.num = num

    # def setName(self, name):
      # self.name = name
    
    # def getName(self):
      # return self.name + " from " + Animal.planet
                
# a1 = Animal("Fish", 10)
# a2 = Animal("Mammal", 20)

# print(a1.type)
# print(a1.planet)

# a2.setName("Tiger")

# print(a2.getName())

class Animal():
    def __init__(self):
        print "Animal created"

    def whoAmI(self):
        print "Animal"

    def eat(self):
        print "Eating"


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print "Dog created"

    def whoAmI(self):
        print "Dog"

    def bark(self):
        print "Woof!"

d = Dog()
d.whoAmI()
d.eat()
d.bark()














