from pages.modal_dialogs import ModalDialogs
import time


#  Тесты запускать по отдельности

def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    assert modal_dialogs.btn_all.check_count_elements(5)


def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()

    modal_dialogs.refresh()
    modal_dialogs.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    time.sleep(2)
    browser.forward()
    assert browser.current_url == 'https://demoqa.com/'
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
