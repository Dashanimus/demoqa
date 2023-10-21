from pages.elements_page import ElementsPage
from pages.demoqa import DemoQA
import time


def test_navigation(browser):
    demo_qa_page = DemoQA(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    (demo_qa_page.btn_elements.click())
    time.sleep(2)

    demo_qa_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert elements_page.equal_url()
