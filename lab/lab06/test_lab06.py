from lab06 import *
import pytest

def test_product():
    with pytest.raises( ValueError ):
        product( 0 )

    with pytest.raises( ValueError ):
        product( 2.5 )

    assert product( 3 ) == 6


def test_summation():
    with pytest.raises( ValueError ):
        summation( -1 )

    with pytest.raises( ValueError ):
        summation( 2.5 )

    assert summation( 3 ) == 6


def test_square():
    assert square( 2 ) == 4

    assert square( 0 ) == 0


def test_sqrt():
    assert sqrt( 4 ) == 2

    assert sqrt( 9 ) == 3


def test_mean():
    assert mean( [ 1 , 2 , 3 , 4 , 5 , 6 ] ) == ( 21 / 6 )

    assert mean( [ 1 , 1 , 1 , 1 , 1 ] ) == 1

    assert mean( [ 0 , 0 , 0 , 0 , 0 ] ) == 0


def test_median():
    assert median( [ 1 , 2 , 3 , 4 , 5 ] ) == 3

    assert median( [ 1 , 3 , 2 , 4 , 5 ] ) == 3

    assert median( [ 1 , 2 , 3 , 4 , 5 , 6 ] ) == 3.5


def test_mode():
    assert mode( [ 1 , 1 , 2 , 3 , 4 , 5 ] ) == 1

    assert mode( [ 1 , 1 , 2 , 2 ] ) == 1


def test_std_dev():
    assert std_dev( [ 1 , 2 , 3 , 4 , 5 ]) == sqrt( 2 )

    assert std_dev( [ 1 , 1 , 1 , 1 , 1 ] ) == 0


def test_stat_analysis():
    assert isinstance( stat_analysis( [ 1 , 1 , 1 , 1 , 1 ] ) , dict )


# OPTIONAL
#####################################

def test_accumulate():
    """Write your code here"""


def test_product_short():
    """Write your code here"""


def test_summation_short():
    """Write your code here"""


def test_invert():
    """Write your code here"""


def test_change():
    """Write your code here"""


def test_invert_short():
    """Write your code here"""


def test_change_short():
    """Write your code here"""
