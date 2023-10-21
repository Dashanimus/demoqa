from pages.webtables import WebTables
import time


def test_webtables_next(browser):
    tables = WebTables(browser)
    tables.visit()

    tables.str_five.click()
    time.sleep(2)

    assert tables.next.get_dom_attribute('disabled')
    assert tables.previous.get_dom_attribute('disabled')

    for i in range(3):
        tables.btn_add.click()
        tables.fill_form()
        tables.submit.click()
        time.sleep(2)

    assert tables.total_page.get_text() == '2'
    assert not tables.next.get_dom_attribute('disabled')
    time.sleep(2)

    tables.next.click()
    assert tables.current_page.get_dom_attribute('value') == '2'
    tables.previous.click()
    assert tables.current_page.get_dom_attribute('value') == '1'
