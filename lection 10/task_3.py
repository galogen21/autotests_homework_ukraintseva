# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize('a, b, expected', [
    pytest.param(-30, 5, -6, marks=pytest.mark.skip),
    (5, 0, ZeroDivisionError),
    pytest.param(25, 5, 5, marks=pytest.mark.smoke),
    (1872, 52, 36),
    ('jjjj', 'rrrrrr', TypeError)
])
def test_all_division(a, b, expected):
    try:
        assert expected == all_division(a, b)
    except Exception:
        with pytest.raises(Exception):
            all_division(a, b)
