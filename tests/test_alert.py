from pages.alerts import Alerts
import time


def test_alert(browser):  # Проверка видимости Alert
    Alert = Alerts(browser)
    Alert.visit()

    assert not Alert.alert()

    Alert.alert_btn.click()
    time.sleep(2)
    assert Alert.alert()
    Alert.alert().accept()


def test_alert_text(browser):  # Подтверждение алерта
    alertText = Alerts(browser)
    alertText.visit()

    alertText.alert_btn.click()
    assert alertText.alert().text == 'You clicked a button'
    alertText.alert().accept()
    assert not alertText.alert()


def test_confirm(browser):  # Отмена Alert
    alertConfirm = Alerts(browser)

    alertConfirm.visit()
    alertConfirm.confirm_btn.click()
    time.sleep(2)
    alertConfirm.alert().dismiss()
    assert alertConfirm.conf_result.get_text() == 'You selected Cancel'
    time.sleep(2)


def test_prompt(browser):  # Проверка ввода текста в Alert
    alert_page = Alerts(browser)
    alert_page.visit()

    alert_page.prompt_btn.click()
    time.sleep(2)
    alert_page.alert().send_keys('Hey')
    alert_page.alert().accept()
    assert alert_page.prompt_form_check.get_text() == 'You entered Hey'
