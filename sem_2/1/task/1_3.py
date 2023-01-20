"""
Класс чудо список.

- можно печатать
- можно сортировать
- можно находить индекс элемента


например
a = MyList([1, 2, 3])
a.print()
a.sort()
a.bin(3)
"""


class MiracleList:

    def __init__(self, data):
        pass

    def get_data(self):
        """
        вернуть список
        """
        pass

    def sort(self):
        """
        отсортировать
        """
        pass

    def bin(self, el):
        """
        поиск номера элемента в отсортированном массиве
        """
        pass


def test_get_data():
    ml = MiracleList([1, 2, 3])
    assert ml.get_data() == ml


def test_sort():
    ml = MiracleList([2, 3, 1])
    ml.sort()
    assert ml.get_data() == [1, 2, 3]


def test_bin():
    ml = MiracleList([2, 3, 1])
    ml.sort()
    assert ml.bin(1) == 1
