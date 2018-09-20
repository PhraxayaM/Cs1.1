class Dog:
    # def bark(self):
    greeting = "Wolf!"

    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Wolf!")






my_first_dog = Dog("Annie")
my_second_dog = Dog("Wyatt")
number2 = Dog(2)

print(my_first_dog.name)
print(my_second_dog.name)
print(number2.name)
my_first_dog.bark()
my_second_dog.bark()

my_dog = Dog("Hey")
my_dog.bark()

if __name__ == "__main__":
    my_dog = Dog("hey")
    my_dog.bark()







print(__name__)
