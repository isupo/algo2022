class my_stack:
    """
    Необходимо написать несложную эмуляцию стека на list
    При эмуляции будем создавать пустой массив следующим образом: [None] * max_size

    """

    def push(self, el):
        """
        добавляет el в стек
        """
        pass

    def pop(self, el):
        """
        удаляет элемент в стеке и возращает его
        """
        pass

    def size(self):
        """
        возращает размер стека
        """
        pass


def test_1():
    s = my_stack()
    s.push(1)
    assert s.pop() == 1


test_1()


def test_2():
    s = my_stack()
    s.push(1)
    assert s.size() == 1


test_2()


def test_3():
    s = my_stack()
    s.push(1)
    s.push(2)
    s.pop()
    s.push(3)
    s.push(4)
    assert s.pop() == 4
    assert s.size() == 2
    assert s.pop() == 3


test_3()
