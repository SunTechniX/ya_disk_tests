from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    # def __init__(self, *args, **kwargs):
    #    super(BasketPage, self).__init__(*args, **kwargs)

    def should_not_be_basket_summary(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_SUMMARY), \
           "Basket summary is presented, but should not be"

    def should_be_empty_basket_msg(self):
        basket_mark = self.browser.find_element(*BasePageLocators.BASKET_EMPTY)
        assert '" ' not in basket_mark.text, "Basket is NOT empty - NO empty message"