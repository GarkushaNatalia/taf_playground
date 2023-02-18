from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(1)>.alertinner')
    BASKET_MESSAGE = (By.CSS_SELECTOR, '.alert-info>.alertinner>p:nth-child(1)')
    BOOK_TITLE = (By.CSS_SELECTOR, '.product_main>h1')
    BOOK_PRICE = (By.CSS_SELECTOR, 'p.price_color')
