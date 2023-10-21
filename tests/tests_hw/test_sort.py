from pages.webtables import WebTables
from conftest import browser


def test_sort(browser):
    tables = WebTables(browser)
    tables.visit()

    for elements in tables.btn_columns.find_elements():
        assert '-sort-asc' not in elements.get_dom_attribute('class')
        assert '-sort-desc' not in elements.get_dom_attribute('class')
        elements.click()
        assert '-sort-asc' not in elements.get_dom_attribute('class')
        assert '-sort-desc' not in elements.get_dom_attribute('class')
