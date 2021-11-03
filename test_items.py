import time

def test__guest_should_see_basket_button(browser):
    browser.get(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.implicitly_wait(10)
    assert browser.find_element_by_class_name('btn-add-to-basket')
    time.sleep(30)
