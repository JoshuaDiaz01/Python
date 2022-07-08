class Pet:
# implement __init__( name , type , tricks ):
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound
    def __init__(self,name,type,tricks,noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health= 100
        self.energy = 50
        self.noise = noise


    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health +=10
        return self
    
    def play(self):
        self.health +=5
        self.energy -= 15
        return self

    def noise(self):
        print(self.noise)



class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        if (len(self.pet_food)) > 0:
            food = self.pet_food.pop()
            print(f'feeding: {self.pet.name} {food}')
            self.pet.eat()
        else:
            print("you need more pet food")
        return self
    
    def bathe(self):
        self.pet.noise()
        return self

my_treats = ['bacon', 'sausage', 'trash']
my_pet_food = ['pizza', 'burger', 'hot dog']
nibbles = Pet("mr. nibbles", 'horse', 'invisible', 'haaay')
adrien = Ninja ('adrien', 'osua', my_treats, my_pet_food, nibbles)

adrien.feed()