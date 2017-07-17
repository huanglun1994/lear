# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'


class Car:
    """"一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化类属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """定义一个方法描述汽车的信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """定义一个方法读取里程"""
        print("\nThis car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """定义一个方法更新里程"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("\nYou can't roll back an odometer!")

    def increment_odometer(self, miles):
        """定义一个方法增加里程"""
        self.odometer_reading += miles


class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("\nThis car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            mileage = 240
        elif self.battery_size == 85:
            mileage = 270
        message = "\nThis car can go approximately " + str(mileage) + " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """检查电瓶容量，如果不是85就设置为85"""
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    """电动汽车的独特之处，继承自汽车类"""
    def __init__(self, make, model, year):
        """初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()

# 创建一个电动车实例对象，电瓶容量为默认值
my_tesla = ElectricCar('tesla', 'model s', 2016)
# 调用方法指出电瓶的续航里程
my_tesla.battery.get_range()
# 调用方法对电瓶进行升级，然后再调用方法显示电瓶的续航里程
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
