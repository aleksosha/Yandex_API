from unittest.mock import Mock

#Пример кода
#class Order:

    #def __init__(self):
        #self.mockachino = None        # сколько пользователь заказал моккачино
        #self.americano = None         # сколько — американо
        #self.sugar = None             # нужно ли добавить сахар и молоко
        #self.milk = None

def test_sugar():
    mock_one = Mock()
    mock_one.configure_mock(sugar='1 ложка')
    assert mock_one.sugar == '1 ложка'