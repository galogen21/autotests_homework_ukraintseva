import pytest

@pytest.mark.usefixtures('start_tests_class')
class Test_My_Class():

    def test_1(self):
        assert 5 * 5 != 0

    def test_2(self):
        assert 5 * 5 == 25

    def test_3(self, end_tests):
        assert 5 * 5 < 50

    def test_4(self):
        assert 5 * 5 > 5
