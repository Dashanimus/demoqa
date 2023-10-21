from pages.elements_page import ElementsPage
from pages.demoqa import DemoQA
import time


def test_go_to_page_elements(browser):
    demo_qa_page = DemoQA(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.btn_elements.click()
    time.sleep(2)
    assert elements_page.equal_url()
