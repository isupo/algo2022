
class Person:
    """
    Просто что-то о человеке
    """
    height = 150
    weight = 50

    def __init__(self, height: int, weight: float):
        if height < 10 or height > 272:
            raise BaseException()
        if weight <= 0 or weight > 500:
            raise BaseException()
        self.height = height
        self.weight = weight

    def get_imt(self):
        return self.weight / ((self.height / 100) ** 2)

    def get_imt_status(self):
        if get_imt > 40:
            return "Ожирение 3-ой степени"
    def print(self):
        print(f"""рост: {self.height}
вес: {self.weight}
        """)

p = Person(weight=222, height=185)
p.print()
print(p.get_imt())
print(p.get_imt_status())
# assert int(p.get_imt()) == 48