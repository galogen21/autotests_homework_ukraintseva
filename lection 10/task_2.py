# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.smoke
def test_zero_exc():
    with pytest.raises(ZeroDivisionError):
        all_division(5, 0)

@pytest.mark.smoke
def test_ok1():
    assert all_division(25, 5) == 5

def test_ok2():
    assert all_division(1872, 52) == 36

def test_type_exc():
    with pytest.raises(TypeError):
        all_division('jjjj', 'rrrrrr')
def test_ok_minus():
    assert all_division(-30, 6) == -5
