class Person:
    def __init__(self):
        self.ability=1
    def eat(self):
        print('Eat: ',self.ability)
    def sleep(self):
        print('Sleep: ',self.ability)
    def study(self):
        print('Study: ', self.ability)
class Wang(Person):
    def eat(self):
        print('Eat: ',self.ability*2)
class Zhang(Person):
    def sleep(self):
        print('Sleep: ',self.ability*2)
class Ming(Person):
    def study(self):
        print('Study: ',self.ability*2)
class Mixture(type):
    def __new__(mcs, *args, **kwargs):
        name,bases,attr=args[:3]
        person1,person2,person3=bases
        def eat(self):
            person1.eat(self)
