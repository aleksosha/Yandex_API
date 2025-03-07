from unittest.mock import Mock

#Пример кода
#class Order:

    #def __init__(self):
        #self.mockachino = None        # сколько пользователь заказал моккачино
        #self.americano = None         # сколько — американо
        #self.sugar = None             # нужно ли добавить сахар и молоко
        #self.milk = None

#Обращаемся к объекту напрямую
def test_mockachino():
    mock_one = Mock()
    mock_one.mokachino = '1 чашка'
    assert mock_one.mokachino == '1 чашка'