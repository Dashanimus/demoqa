from pages.demoqa import DemoQA
import time


def test_size(browser):
    demo_qa_page = DemoQA(browser)
    demo_qa_page.visit()
    browser.set_window_size(width=1000, height=300)
    time.sleep(2)
    browser.set_window_size(width=1000, height=1000)
