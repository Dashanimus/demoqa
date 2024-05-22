from pages.browser_tab import BrowserTab
from pages.accordian import Accordian
from pages.alerts import Alerts
from pages.demoqa import DemoQA
import pytest
import time


def test_check_title_demo(browser):
    demo_qa_page = DemoQA(browser)
    demo_qa_page.visit()
    assert demo_qa_page.get_title() == 'DEMOQA'

    @pytest.mark.parametrize("pages", [Accordian, Alerts, DemoQA, BrowserTab])
    def test_check_title_all_pages(browser, pages):
        page = pages(browser)
        page.visit()
        time.sleep(2)
        assert browser.title == 'title'
