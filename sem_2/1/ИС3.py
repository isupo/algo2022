class Person:
    """
    шото можем тут написать
    """
    height: int = 181
    weight: int = 85

    def __init__(self, height: int = 180, weight: int = 85):
        if height < 35 or height > 272:
            raise BaseException()

        if height <= 0 or height > 610:
            raise BaseException()

        self.height = height
        self.weight = weight
        self.check_imt()

    def check_imt(self):
        self.imt = self.weight / ((self.height / 100) ** 2)

    def set_height(self, height):
        if height < 35 or height > 272:
            raise BaseException()

        self.height = height
        self.check_imt()

    def get_height(self):
        return self.height

    def get_imt(self):
        return self.imt

    def eat_bur(self):
        self.weight += 0.5
        self.check_imt()

    def go_gim(self):
        self.weight -= 0.2
        self.check_imt()


p = Person(176, 64)
print(p.get_imt())
p.set_height(177)
print(p.get_imt())
print('Го съедим булку')
p.eat_bur()
print(p.get_imt())
print('Го Джим')
p.go_gim()
print(p.get_imt())
print('Го Джим')
p.go_gim()
print(p.get_imt())
print('Го Джим')
p.go_gim()
print(p.get_imt())
print('Го Джим')
p.go_gim()
print(p.get_imt())
print('Го Джим')
p.go_gim()
print(p.get_imt())
