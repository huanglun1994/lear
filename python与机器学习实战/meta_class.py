class Person:
    def __init__(self):
        self.ability = 1

    def eat(self):
        print('Eat: ', self.ability)

    def sleep(self):
        print('Sleep: ', self.ability)

    def study(self):
        print('Study: ', self.ability)


class Wang(Person):
    def eat(self):
        print('Eat: ', self.ability * 2)


class Zhang(Person):
    def sleep(self):
        print('Sleep: ', self.ability * 2)


class Ming(Person):
    def study(self):
        print('Study: ', self.ability * 2)


class Mixture(type):
    def __new__(mcs, *args, **kwargs):
        name, bases, attr = args[:3]
        person1, person2, person3 = bases

        def eat(self):
            person1.eat(self)

        def sleep(self):
            person2.sleep(self)

        def study(self):
            person3.study(self)

        for key, value in locals().items():
            if str(value).find('function') >= 0:
                attr[key] = value
        return type(name, bases, attr)


def test(person):
    person.eat()
    person.sleep()
    person.study()


class Hong(Wang, Zhang, Ming, metaclass=Mixture):
    pass


test(Hong())  # 将会输出三行，依次是Eat:2 Sleep:2 和Study:2


class Hong(Zhang, Wang, Ming, metaclass=Mixture):
    pass


test(Hong())  # 将会输出三行，依次是Eat:1 Sleep:1 和Study:2
