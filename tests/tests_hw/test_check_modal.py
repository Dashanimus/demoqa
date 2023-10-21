from pages.modal_dialogs import ModalDialogs
from conftest import browser
#import pytest
import time


#@pytest.mark.skipif(True, reason='просто пропуск')
def test_check_modal(browser):
    modal_check = ModalDialogs(browser)
    #code_status = modal_check.code_status()

    # if code_status != 200:
    #     pytest.skip(reason=f"Страница{modal_check.base_url} недоступна")
    # print(code_status)

    modal_check.visit()
    len_list = len(modal_check.list_btn.find_elements())
    list_btn = modal_check.list_btn.find_elements()
    list_name_btn = []

    for item in list_btn:
        list_name_btn.append(item.text)
    assert "Small modal" and "Large modal" in list_name_btn  # Проверяем наличие двух кнопок (Small modal и Large modal)
    assert len_list == 2
    modal_check.btn_small_modal.click()
    time.sleep(3)

    assert modal_check.body_small_modal.get_text() == "This is a small modal. It has very less content"
    assert modal_check.btn_close_small_modal.visible()  # Проверка, что открылось small_modal
    modal_check.btn_close_small_modal.click()
    time.sleep(2)

    modal_check.btn_large_modal.click()
    len_body = len(modal_check.body_large_modal.get_text())
    print("Количество символов ", len_body)

    assert len_body == 574  # Проверка, что окно large-modal открыто
    assert modal_check.body_large_modal.visible()  # Открылось окно large_modal
    assert modal_check.btn_close_large_modal.visible()
    time.sleep(2)
    modal_check.btn_close_large_modal.click()
    time.sleep(2)
