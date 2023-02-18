import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                          ])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_card()
    page.should_be_success_message()
    page.should_be_book_title_in_success_message()
    page.should_be_book_price_in_basket_message()


@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_card()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_card()
    page.should_disappear_success_message()
