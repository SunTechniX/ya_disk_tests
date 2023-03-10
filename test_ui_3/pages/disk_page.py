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

    def go_to_top_button_copy(self):
        link = self.browser.find_element(*DiskPageLocators.TOP_BUTTON_COPY)
        link.click()

    def go_to_top_button_delete(self):
        link = self.browser.find_element(*DiskPageLocators.TOP_BUTTON_DELETE)
        link.click()

    def go_to_disk_root_dir(self):
        link = self.browser.find_element(*DiskPageLocators.DISK_DIR_ROOT)
        link.click()

    def go_to_dlg_root_dir(self):
        link = self.browser.find_element(*DiskPageLocators.DLG_DIR_ROOT)
        link.click()

    def go_to_dlg_button_copy(self):
        link = self.browser.find_element(*DiskPageLocators.DLG_BUTTON_COPY)
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
        print('Action Over New Dir', link.text)

    def go_to_dialog(self): # not used ?
        link = self.browser.find_element(*DiskPageLocators.DISK_CREATE)
        link.click()

    def go_to_dialog_close_click(self):
        link = self.browser.find_element(*DiskPageLocators.DLG_BUTTON_CLOSE)
        link.click()

    def create_obj(self, name='my_name'):
        ed_name = self.browser.find_element(*DiskPageLocators.DISK_OBJ_NAME)
        ed_name.click() # set focus on edit field
        ed_name.clear() # whi this not working
        ed_name.send_keys(Keys.CONTROL + "a")
        #ed_name.send_keys(Keys.SHIFT, Keys.ARROW_UP)
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

    def go_to_dlg_dir_select(self, name='dir_name'):
        link = self.browser.find_element(*DiskPageLocators.get_DLG_DIR_TITLE_selector(self, name))
        link.click()
        ## self.browser.execute_script("return arguments[0].scrollIntoView(true);", link)
        #action = ActionChains(self.browser)
        #action.move_to_element(link)
        #action.double_click(link)
        #action.perform()

    def go_to_disk_file_click(self, name):
        link = self.browser.find_element(*DiskPageLocators.get_DISK_ITEMS_TITLE_selector(self, name))
        print(link.get_attribute('aria_label'))
        #link.click()
        #self.browser.execute_script("return arguments[0].scrollIntoView(true);", link)
        action = ActionChains(self.browser)
        action.move_to_element(link)
        action.click(link)
        action.perform()

    #def id_item_object(self, obj_name='obj_name'):
    #    obj_except = self.is_element_present(*DiskPageLocators.get_DISK_ITEMS_TITLE_selector(self, obj_name))
    #    print('>>id>>', obj_except.id, obj_except.text)

    #def id_item_objects(self):
    #    items = self.browser.find_elements(*DiskPageLocators.DISK_ITEMS_FILE_TITLE)
    #    for item in items:
    #        attr_value = item.get_attribute('title')
    #        #attr_value = item.get_attribute('aria_label')
    #        print('>>>>', "'", attr_value, "'")  # item.id, item.text

    def del_list_objects_except(self, name_obj_except='obj_name'):
        items = self.browser.find_elements(*DiskPageLocators.DISK_ITEMS_FILE_TITLE)
        for item in items:
            #print(item.text, name_obj_except)
            if item.get_attribute('title') != name_obj_except:
                action = ActionChains(self.browser) # а-ля go_to_disk_file_click()
                action.move_to_element(item)
                action.click(item)
                action.perform()
                self.should_be_top_button_delete()
                self.go_to_top_button_delete()

    #def get_list_objects(self):
    #    items = self.browser.find_elements(*DiskPageLocators.DISK_ITEMS)
    #    print('>>>>>>>>>>>', len(items))
    #    #for each_item in items:
    #    #listing = self.browser.find_element(*DiskPageLocators.DISK_LISTING)
    #    print('>>>>>>>>>>>', items) #***

    def go_to_logout(self):
        self.go_to_disk_login_page()
        link = self.browser.find_element(*DiskPageLocators.LOGOUT_LINK)
        link.click()

    def is_ad_flash_show(self):
        return self.is_element_present_silent(*DiskPageLocators.AD_FLASH)

    def is_dlg_show(self):
        return self.is_element_present_silent(*DiskPageLocators.DLG_BUTTON_CLOSE)

    def scroll_to_top_button_copy(self):
        link = self.browser.find_element(*DiskPageLocators.TOP_BUTTON_COPY)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", link)
        #reserv# ActionChains(self.browser).scroll_to_element(link).perform()

    def should_be_authorized_user(self): # like BasePage.should_be_authorized_user()
        self.go_to_disk_login_page() # like BasePage.go_to_flash_login_page()
        assert self.is_element_present(*DiskPageLocators.LOGIN_SUCCESS),\
            "User Avatar/icon is not presented," \
            " Probably unauthorised user"

    def should_be_top_button_info(self):
        assert self.is_element_present(*DiskPageLocators.TOP_BUTTON_INFO), "INFO Button is not presented"

    def should_be_top_button_copy(self):
        assert self.is_element_present(*DiskPageLocators.TOP_BUTTON_COPY), "Copy Button is not presented"

    def should_be_top_button_delete(self):
        assert self.is_element_present(*DiskPageLocators.TOP_BUTTON_DELETE), "Delete Button is not presented"

    def should_be_top_button_more(self):
        assert self.is_element_present(*DiskPageLocators.TOP_BUTTON_MORE), "MORE Button is not presented"

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

    def should_be_disk_obj_name(self, name='obj_name'):
        assert self.is_element_present(*DiskPageLocators.get_DISK_ITEMS_TITLE_selector(self, name)),\
            f"DISK OBJ name '{name}' is not presented"

    def should_be_dlg_obj_name(self, name='obj_name'):
        assert self.is_element_present(*DiskPageLocators.get_DLG_DIR_TITLE_selector(self, name)),\
            f"DLG OBJ name '{name}' is not presented"


