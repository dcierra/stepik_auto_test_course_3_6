from selenium.webdriver.common.by import By


def test_check_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    browser.implicitly_wait(5)
    assert browser.find_elements(By.XPATH, "//form[@id='add_to_basket_form']/button"), 'Basket Button Not Found'