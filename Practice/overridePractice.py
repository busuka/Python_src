class Animal():

    def __init__(self, names):
        self.names = names

    def barks(self):
        print("動物の名前は" + self.names)


class Dog(Animal):

    def barks(self):
        print("わんわん")

dog1 = Animal("dog")
print(dog1.names)
dog1.barks()

dog2 = Dog("dog")
print(dog2.names)
dog2.barks()