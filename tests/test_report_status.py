import allure
import pytest


@allure.feature('проверка статусов тестов')
def test_success():
    assert True


@allure.feature('проверка статусов тестов')
def test_failure():
    assert False


@allure.feature('проверка статусов тестов')
def test_skip():
    pytest.skip('...')


@allure.feature('проверка статусов тестов')
def test_broken():
    raise Exception('oops')  # Raise для создания искусственной ошибки