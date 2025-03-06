from byu_pytest_utils import max_score, with_import
import pytest


@max_score(5)
@with_import('lab07', 'exception_handler')
def test_exception_handler(exception_handler, capsys):
    exception_handler()
    captured = capsys.readouterr()
    observed = captured.out.strip()
    assert "<class 'TypeError'>" in observed


@max_score(3)
@with_import('lab07', 'in_range1')
def test_in_range1(in_range1):
    assert in_range1(9)
    assert not in_range1(-4)
    assert not in_range1(103)


@max_score(3)
@with_import('lab07', 'in_range2')
def test_in_range2(in_range2):
    in_range2(9)
    with pytest.raises(ValueError):
        in_range2(-4)
        pytest.fail("in_range2(-4) didn't raise an exception")

    with pytest.raises(ValueError):
        in_range2(103)
        pytest.fail("in_range2(103) didn't raise an exception")


@max_score(4)
@with_import('lab07', 'main')
def test_main_loop(main, monkeypatch):
    call_count = 0

    def mock_randint(a, b):
        nonlocal call_count
        call_count += 1
        return 1

    monkeypatch.setattr('random.randint', mock_randint)
    main()
    assert call_count == 1000, f"Expected 1000 random calls, got {call_count}"


@max_score(5)
@with_import('lab07', 'bound_checker')
def test_bound_checker(bound_checker):
    assert bound_checker(10, 12, 2, 3)
    with pytest.raises(IndexError):
        bound_checker(10, 12, 59, 3)
        pytest.fail("bound_checker(10, 12, 59, 3) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, 2, 13)
        pytest.fail("bound_checker(10, 12, 2, 13) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, -1, 3)
        pytest.fail("bound_checker(10, 12, -1, 3) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, 2, -1)
        pytest.fail("bound_checker(10, 12, 2, -1) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, 10, 12)
        pytest.fail("bound_checker(10, 12, 10, 12) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, 10, 0)
        pytest.fail("bound_checker(10, 12, 10, 0) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, 0, 12)
        pytest.fail("bound_checker(10, 12, 0, 12) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, 11, 0)
        pytest.fail("bound_checker(10, 12, 11, 0) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, 0, 13)
        pytest.fail("bound_checker(10, 12, 0, 13) didn't raise an exception")
    with pytest.raises(IndexError):
        bound_checker(10, 12, 11, 13)
        pytest.fail("bound_checker(10, 12, 11, 13) didn't raise an exception")
