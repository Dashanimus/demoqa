from pages.webtables import WebTables
import time


def test_webtables(browser):
    # Проверка блока No rows found
    page_tables = WebTables(browser)

    page_tables.visit()
    assert not page_tables.no_data.exist()

    # Удаляем все записи
    while page_tables.btn_delete_row.exist():
        page_tables.btn_delete_row.click()
        time.sleep(2)

    assert page_tables.no_data.exist()
