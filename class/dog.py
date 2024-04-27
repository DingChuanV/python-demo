class Dog():
    """
    一次模拟小狗的简单尝试
    """

    def __init__(self, name, age):
        """
        初始化属性name和age
        """
        self.name = name
        self.age = age

    def sit(self):
        """
        模拟小狗被命令时蹲下
        """
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """
        模拟小狗被命令时打滚
        """
        print(self.name.title() + " rolled over!")


class Car():
    """
    一次模拟汽车的简单尝试
    """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + '' + self.make + '' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """
    电动汽车的独特之处
    """

    def __init__(self, make, model, year):
        """
        初始化父类的属性
        """
        super().__init__(make, model, year)


class Battery():
    """
    一次模拟电动汽车电瓶的简单尝试
    """
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        print(message)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """检查电瓶容量，并使其至少为85"""
        if self.battery_size != 85:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
            return
        print("The battery is already upgraded.")
        return

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """
        检查电瓶容量，并使其至少为85
        """
        if self.battery_size != 85:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
            return
        print("The battery is already upgraded.")
        return


if __name__ == '__main__':
    my_dog = Dog('model', 6)
    print("My dog's name is " + my_dog.name.title() + ".")
    print("My dog is " + str(my_dog.age) + " years old.")
    my_dog.sit()
    my_dog.roll_over()

    my_car = Car('audi', 'a4', 2016)
    print(my_car.get_descriptive_name())
    my_car.update_odometer(23)
    my_car.read_odometer()
    my_car.increment_odometer(100)
    my_car.read_odometer()
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name())

    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
    my_tesla.battery.upgrade_battery()
    my_tesla.battery.get_range()
    my_tesla.battery.upgrade_battery()

