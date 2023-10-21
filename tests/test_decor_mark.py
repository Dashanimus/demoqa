import pytest


@pytest.mark.smoke
def test_1():
    assert True


@pytest.mark.regress
def test_2():
    assert True


@pytest.mark.regress
def test_3():
    assert True


@pytest.mark.regress
def test_4():
    assert True
