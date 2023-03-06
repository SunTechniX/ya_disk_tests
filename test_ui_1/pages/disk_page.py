import pytest
from .base_page import BasePage
from .locators import DiskPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

class DiskPage(BasePage):
    def go_to_disk_login_page(self): # like BasePage.go_to_flash_login_page()
        link = self.browser.find_element(*DiskPageLocators.LOGIN_BTN)
        link.click()

    def go_to_hide_profile(self):
        link = self.browser.find_element(*DiskPageLocators.LOGIN_PROFILE_HIDE)
        link.click()

    def go_to_create_button(self):
        link = self.browser.find_element(*DiskPageLocators.DISK_CREATE)
        link.click()

    def go_to_close_ad_flash(self):
        link = self.browser.find_element(*DiskPageLocators.AD_FLASH_CLOSE_BTN)
        link.click()

    def go_to_dir_plus(self):
        link = self.browser.find_element(*DiskPageLocators.DISK_DIR_PLUS)
        link.click()

    def go_to_file_plus(self):
        link = self.browser.find_element(*DiskPageLocators.DISK_FILE_PLUS)
        link.click()

    def go_to_dir_plus_perform(self):
        link = self.browser.find_element(*DiskPageLocators.DISK_DIR_PLUS)
        print('>>>', link.text)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", link)
        action = ActionChains(self.browser)
        action.move_to_element(link)
        action.click(link)
        action.perform()
        print('Action Over Menu-Item', link.text)

    def go_to_dialog(self): # not used ?
        link = self.browser.find_element(*DiskPageLocators.DISK_CREATE)
        link.click()

    def create_obj(self, name='my_name'):
        ed_name = self.browser.find_element(*DiskPageLocators.DISK_OBJ_NAME)
        ed_name.click() # set focus on edit field
        ed_name.clear() # whi this not working
        #ed_name.send_keys(Keys.CONTROL + "a")
        ed_name.send_keys(Keys.SHIFT, Keys.ARROW_UP)
        ed_name.send_keys(Keys.DELETE)
        #self.browser.execute_script("return arguments[0].scrollIntoView(true);", ed_name)
        #while ed_name.text != '':
        #    ed_name.clear()
        #    time.sleep(2)
        #else:
        #    ed_name.clear() # Очистить наверняка!
        ed_name.send_keys(name)
        self.browser.find_element(*DiskPageLocators.DISK_SUBMIT_BTN).click()

    def go_to_inside_dir(self, name='dir_name'):
        link = self.browser.find_element(*DiskPageLocators.get_DISK_ITEMS_TITLE_selector(self, name))
        #link.click()
        #self.browser.execute_script("return arguments[0].scrollIntoView(true);", link)
        action = ActionChains(self.browser)
        action.move_to_element(link)
        action.double_click(link)
        action.perform()

    def get_list_objects(self):
        items = self.browser.find_elements(*DiskPageLocators.DISK_ITEMS)
        print('>>>>>>>>>>>', len(items))
        #for each_item in items:
        #listing = self.browser.find_element(*DiskPageLocators.DISK_LISTING)
        print('>>>>>>>>>>>', items) #***

    def go_to_logout(self):
        self.go_to_disk_login_page()
        link = self.browser.find_element(*DiskPageLocators.LOGOUT_LINK)
        link.click()

    def is_ad_flash_show(self):
        return self.is_element_present_silent(*DiskPageLocators.AD_FLASH)

    def should_be_authorized_user(self): # like BasePage.should_be_authorized_user()
        self.go_to_disk_login_page() # like BasePage.go_to_flash_login_page()
        assert self.is_element_present(*DiskPageLocators.LOGIN_SUCCESS),\
            "User Avatar/icon is not presented," \
            " Probably unauthorised user"

    def should_be_create_button(self):
        assert self.is_element_present(*DiskPageLocators.DISK_CREATE), "Create Button is not presented"

    def should_be_dir_plus(self):
        assert self.is_element_present(*DiskPageLocators.DISK_DIR_PLUS), "Dir Plus Button is not presented"

    def should_be_file_plus(self):
        assert self.is_element_present(*DiskPageLocators.DISK_FILE_PLUS), "File PLus Button is not presented"

    def should_be_dialog(self):
        assert self.is_element_present(*DiskPageLocators.DISK_DIALOG), "Dialog wrap is not presented"

    def should_be_object_edit_field(self):
        assert self.is_element_present(*DiskPageLocators.DISK_OBJ_NAME), "Edit Field is not presented"

    def should_be_submit_button(self):
        assert self.is_element_present(*DiskPageLocators.DISK_SUBMIT_BTN), "Submit Button is not presented"

    def should_be_dialog_form(self):
        self.should_be_dialog()
        self.should_be_object_edit_field()
        self.should_be_submit_button()

    def should_be_obj_name(self, name='obj_name'):
        assert self.is_element_present(*DiskPageLocators.get_DISK_ITEMS_TITLE_selector(self, name)),\
            f"OBJ name '{name}' is not presented"





    def add_product_to_basket(self):
        self.click_on_basket_button()
        #self.solve_quiz_and_get_code()   # Запустить решение и получение кода
        self.solve_quiz_and_get_code_ff()   # Запустить решение и получение кода
        print('sleep 2 sec after solve code')
        time.sleep(2)
        self.check_product_name_in_basket()
        self.check_product_price_in_basket()

    def click_on_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket Button is not presented"
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def check_product_in_basket(self):
        WebDriverWait(self.browser, 5).until(EC.is_element_present(*ProductPageLocators.BASKET_NAME))
        assert WebDriverWait(self.browser, 5).until(
            EC.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
        ), "Product not added to Basket!"

    def check_product_name_in_basket(self):
        name_prod = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name_basket = self.browser.find_element(*ProductPageLocators.BASKET_NAME)
        assert name_prod.text == name_basket.text, "Product name not equal name in Basket!"

    def check_product_price_in_basket(self):
        price_prod = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert price_prod.text == price_basket.text, "Product price not equal price in Basket!"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is present"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be - should is disappeared!"
