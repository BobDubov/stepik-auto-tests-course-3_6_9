import time

def test_5(browser):
    browser.get(f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.implicitly_wait(10)
    assert browser.find_element_by_class_name('btn-add-to-basket').text == "Añadir al carrito"
    time.sleep(30)
