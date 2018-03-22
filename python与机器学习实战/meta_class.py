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


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass
class MyList(list, metaclass=ListMetaclass):
    pass


# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，
# 要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，
# 比如，加上新的方法，然后，返回修改后的定义。
# __new__()方法接收到的参数依次是：当前准备创建的类的对象；类的名字；类继承的父类集合；类的方法集合。
L = MyList()
L.add(1)
print(L)
