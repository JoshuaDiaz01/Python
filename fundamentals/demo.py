from io import BufferedRandom
from turtle import color


class Person:
    def __init__(self, first_name, last_name, height, weight, age, shoe_size ):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
        self.age = age
        self.shoe_size = shoe_size
        self.shoes = []
        self.fullname = f"{first_name} {last_name}"
    def info(self):
        print(f'fullname: {self.fullname}')
        print(f'height: {self.height}')
        print(f'weight: {self.weight}')
        print(f'age: {self.age}')
        print(f'shoe_size: {self.shoe_size}')
        print('shoes:')
        for shoe in self.shoes:
            (shoe.info())
        print('*'*80)
        return self
    def walk(self):
        pass

    def get_shoes(self, shoe):
        if shoe.size != self.shoe_size:
            print("you cant have that shoe")
            return False
        self.shoes.append(shoe)
        print('you have received new shoes')
        return self

class Shoe:
    def __init__(self, brand, color, type, size):
        self.brand = brand
        self.color = color
        self.type = type
        self.size = size
        self.miles = 0
    def info(self):
        print(f'brand: {self.brand}')
        print(f'color: {self.color}')
        print(f'miles: {self.miles}')
        print(f'size: {self.size}')

    
p1 = Person('Joshua', 'diaz', 160, 100, 22, 13)
s1 = Shoe('nike', 'black', 'high', '12')

p1.get_shoes(s1)
p1.info()