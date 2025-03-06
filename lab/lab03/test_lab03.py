from byu_pytest_utils import max_score, with_import
from pytest import approx

@max_score(2)
@with_import('lab03', 'average_temperature')
def test_average_temperature_1(average_temperature):
    assert average_temperature([72.2, 68.7, 67.4, 77.3, 81.6, 83.7]) == approx(75.15)

@max_score(3)
@with_import('lab03', 'average_temperature')
def test_average_temperature_2(average_temperature):
    assert average_temperature([63.4, 70.8, 52.3, 74.6, 69.2, 54.3]) == approx(64.1)

@max_score(2)
@with_import('lab03', 'hot_days')
def test_hot_days_1(hot_days):
    assert hot_days([72.2, 68.7, 67.4, 77.3, 81.6, 83.7]) == 2

@max_score(3)
@with_import('lab03', 'hot_days')
def test_hot_days_2(hot_days):
    assert hot_days([63.4, 70.8, 52.3, 74.6, 69.2, 54.3]) == 3

@max_score(5)
@with_import('lab03', 'is_palindrome')
def test_is_palindrome(is_palindrome):
    assert is_palindrome('rotator')
    assert not is_palindrome('apple')

@max_score(2)
@with_import('lab03', 'even_weighted')
def test_even_weighted_1_2_3_4_5_6(even_weighted):
    assert even_weighted([1, 2, 3, 4, 5, 6]) == [0, 6, 20]

@max_score(3)
@with_import('lab03', 'even_weighted')
def test_even_weighted_9_17_4_5_4(even_weighted):
    assert even_weighted([9, 17, 4, 5, 4]) == [0, 8, 16]