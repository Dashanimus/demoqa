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
    # assert page.metaView.get_dom_attribute('name') == 'viewport'
    # assert page.metaView.get_dom_attribute('content') == 'width=device-width,initial-scale=1'
