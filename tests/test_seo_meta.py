from pages.browser_tab import BrowserTab
from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.demoqa import DemoQA
import pytest
import time


@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQA, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.metaView.exist()
