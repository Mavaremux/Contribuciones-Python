class Animal:
    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass
#SUBCLASES

class dog(Animal):
    def sound(self):
        print("Guau")

class gato(Animal):
    def sound(self):
        print("MiAU")

def print_sound(animal: Animal):
    animal.sound()

my_animal = Animal("Animal")
print_sound(my_animal)
my_dog = dog("Perro")
print_sound(my_dog)
my_cat = gato("Gato")
print_sound(my_cat)

