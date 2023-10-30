class Vehicle():
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage
        self.current_speed = 0

    def increase_speed(self, increase):
        self.max_speed += increase

    def break_speed(self, brake_speed):
        if self.current_speed - brake_speed >= 0:
            self.current_speed -= brake_speed
        else:
            self.current_speed = 0
    def milage_info(self):
        print(f"On odometre -- {self.milage} mp/h\nSpeed: {self.current_speed}")

ob1 = Vehicle(200, 1000)
ob1.increase_speed(20)
ob1.break_speed(200)
print(ob1.milage_info())

ob2 = Vehicle(200, 1000)
ob2.increase_speed(150)
ob2.break_speed(300)
print(ob2.milage_info())

class Animal:
    def __init__(self, firstname, lastname, weight, eyes):
        self.firstname = firstname
        self.lastname = lastname
        self.weight = weight
        self.eyes = eyes

    def jump(self):
        return f"{self.firstname} {self.lastname} is jumping"

    def eat(self, food):
        return f"{self.firstname} {self.lastname} is eating {food}"

    def breath(self):
        return f"{self.firstname} {self.lastname} is breathing"


ob3 = Animal("black", "cat", 8, 2)
print(ob3.jump())
print(ob3.eat("my eat"))
print(ob3.breath())

ob4 = Animal("brown", "bear", 300, 2)
print(ob4.jump())
print(ob4.eat("honey"))
print(ob4.breath())