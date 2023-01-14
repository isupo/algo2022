class Person():
    height: 120
    weight: 70

    def __init__(self, height: int, weight: int):
        self.set_height(height)
        self.weight = weight

    def get_imt(self):
        return self.weight / ((self.height / 100) ** 2)

    def print(self):
        print(f"""Рост {self.height}, вес {self.weight}""")

    def set_height(self, height):
        if height > 272 or height < 10:
            raise BaseException()
        self.height = height


bw = Person(175, 57)
bw.print()
bw.set_height(176)
bw.print()
