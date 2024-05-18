from pages.demoqa import DemoQa
from pages.elements import Elements
def test_navigation(browser):
    demo = DemoQa(browser)
    element = Elements(browser)


    demo.visit()
    demo.button_elements.click()

    element.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert element.equal_url()




