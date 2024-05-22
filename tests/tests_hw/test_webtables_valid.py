from pages.webtables import WebTables
import time


def test_webtables_valid(browser):
    tables = WebTables(browser)
    tables.visit()

    assert tables.btn_add.exist()
    tables.btn_add.click()
    assert tables.modal_dialog.visible()

    tables.submit.click()
    assert tables.modal_dialog.visible()

    assert 'example@mail.com' not in tables.table.get_text()
    tables.fill_form()
    time.sleep(2)
    tables.submit.click()
    time.sleep(2)
    assert not tables.modal_dialog.exist()
    time.sleep(2)

    assert 'example@mail.com' in tables.table.get_text()

    tables.btn_edit_4.click()
    assert tables.inp_mail.get_dom_attribute('value') == 'example@mail.com'
    time.sleep(2)

    tables.inp_mail.clear()
    tables.inp_mail.send_keys('example@mail.com')
    tables.submit.click()
    assert 'example@mail.com' in tables.table.get_text()

    tables.btn_delete_4.click()
    assert 'example@mail.com' not in tables.table.get_text()
