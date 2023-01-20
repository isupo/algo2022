'''
Реализовать крестики-нолики
Название
TikTacToe
функции
place_crosses
place_noughts
get_winner
'''


class TikTacToe:
    def place_crosses(self, x, y):
        """
        Должен вернуть 1, если всё ок. Или 0, если нельзя осуществить операцию
        """
        pass

    def place_noughts(self, x, y):
        """
        Должен вернуть 1, если всё ок. Или 0, если нельзя осуществить операцию
        """
        pass

    def get_winner(self):
        """
        Вернуть
        0 нет победителя
        1 победили crosses
        0 победили noughts
        """
        pass


def test_1():
    game = TikTacToe()
    assert game.place_crosses(1, 3) == 1
    assert game.place_crosses(1, 3) == 0
