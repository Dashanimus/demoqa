from pages.demoqa import DemoQA


def test_icon_exist(browser):
    demo_qa_page = DemoQA(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    # demo_qa_page.click_on_the_icon()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.icon.exist()

    # browser = webdriver.Chrome()
    # browser.get("http://demoqa.com/")
    #
    # try:
    #     browser.find_element(By.CSS_SELECTOR, '#app > header > a') #icon =
    # except NoSuchElementException:
    #     assert False
    # assert True
