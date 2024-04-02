# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
from datetime import datetime

@pytest.fixture(scope='class')
def start_tests_class():
    print(datetime.now())
    yield
    print(datetime.now())

@pytest.fixture()
def time_tests():
    start = datetime.now()
    yield start

@pytest.fixture()
def end_tests(time_tests):
    yield
    print('time:', datetime.now() - time_tests)







