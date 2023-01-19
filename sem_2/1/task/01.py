class Car:
    """
    класс автомобиль
    """
    color = 'white'  # цвет
    engine_power = 90  # мощность двигателя
    tank_capacity = 50  # объем бака
    fuel_consumption = 9.3  # расход топлива на 100 км
    fuel_now = 0  # топлива в баке сейчас

    def __init__(self):
        pass

    def set_color(self, color):
        """
        перекрасить автомобиль
        """
        pass

    def get_color(self):
        """
        узнать цвет
        """
        pass

    def get_fuel_now(self):
        """
        :return: топлива есть сейчас
        """
        pass

    def refuel(self, liters_of_fuel):
        """
        заправить liters_of_fuel топлива
        :param liters_of_fuel:
        :return:
        """
        pass

    def get_engine_power(self):
        """
        узнать мощность двигателя
        :return:
        """
        pass

    def get_fuel_consumption(self):
        """
        узнать расход топлива
        :return:
        """
        pass


def test_init_1():
    Car(color='white',
        engine_power=90,
        tank_capacity=50,
        fuel_consumption=9.3,
        fuel_now=0)


def test_init_2():
    Car(color='white')


def test_color_1():
    c = Car(color='white',
            engine_power=90,
            tank_capacity=50,
            fuel_consumption=9.3,
            fuel_now=0)
    assert c.get_color() == 'white'


def test_color_2():
    c = Car(color='white',
            engine_power=90,
            tank_capacity=50,
            fuel_consumption=9.3,
            fuel_now=0)
    assert c.get_color() == 'white'
    c.set_color('red')


def test_color_3():
    c = Car(color='white',
            engine_power=90,
            tank_capacity=50,
            fuel_consumption=9.3,
            fuel_now=0)
    assert c.get_color() == 'white'
    c.set_color('red')

    assert c.get_color() == 'red'
