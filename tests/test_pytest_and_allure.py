import pytest


@pytest.mark.skip(reason='Причина пропуска')
def test_skip():
    assert True


@pytest.mark.xfail(condition=True, reason='Причина, по которой тестовая функция помечена xfail')
def test_xfail_1():
    # Если тест упадёт - метка skipped - тест пропущен
    # Если тест пройдёт - passed
    # В обоих случаях в отчёт добавится тег ожидаемый сбой
    assert False


@pytest.mark.xfail(condition=True, reason='Причина, по которой тестовая функция помечена xfail')
def test_xfail_2():
    assert True


@pytest.mark.skipif(condition='2 + 2 != 5')
def test_skip_by_triggered_condition():
    pass


@pytest.mark.parametrize('param', [1, 2, 3, 4, 6])
def test_parametrize(param):
    assert (param % 2) == 0
