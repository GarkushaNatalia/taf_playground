from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_card(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented"

    def should_be_book_title_in_success_message(self):
        title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        message_text = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert title in message_text, f'{title} is not in {message_text}'

    def should_be_book_price_in_basket_message(self):
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        message_text = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE).text
        assert price in message_text, f'{price} is not in {message_text}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
