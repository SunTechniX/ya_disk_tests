from selenium.webdriver.common.by import By

class BasePageLocators():
    TIMEOUT = 10
    CAPTCHA_FORM = (By.CSS_SELECTOR, '#checkbox-captcha-form')
    LOGIN_BTN = (By.CSS_SELECTOR, ".dzen-header-desktop__profileMenu-3q")
    LOGIN_SUCCESS = (By.CSS_SELECTOR, "div.zen-ui-avatar")

class LoginPageLocators():
    LOGIN_FLASH_FORM = (By.CSS_SELECTOR, ".login-content__container-g1")
    LOGIN_FLASH_FORM_BTN_YID = (By.CSS_SELECTOR, ".login-content__yaButton-2A")
    #LOGIN_FLASH_FORM_BTN_YID = (By.CSS_SELECTOR, ".base-login-button__loginButton-xC")
    LOGIN_FORM = (By.CSS_SELECTOR, '.passp-auth-content')
    LOGIN_FORM_MODE_BUTTON = (By.CSS_SELECTOR, 'button[data-type="login"]') # button[data-t="button:default"]
    LOGIN_FORM_USER_NAME = (By.CSS_SELECTOR, 'input[name="login"]')
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, 'input[data-t="field:input-passwd"]')
    LOGIN_FORM_SIGN_IN_BTN = (By.CSS_SELECTOR, 'button[data-t="button:action:passp:sign-in"]')
    LOGIN_FORM_PSEUDO_BTN = (By.CSS_SELECTOR, 'button[data-t="button:pseudo"]')

class DiskPageLocators():
    LOGIN_BTN = (By.CSS_SELECTOR, "a.user-account")
    LOGIN_SUCCESS = (By.CSS_SELECTOR, 'img.user-pic__image')
    LOGOUT_LINK = (By.CSS_SELECTOR, 'a.legouser__menu-item_action_exit')
    DISK_CREATE = (By.CSS_SELECTOR, 'span.create-resource-popup-with-anchor > button')
    DISK_DIR_PLUS = (By.CSS_SELECTOR, 'button > span.create-resource-button__text')
    #DISK_DIR_PLUS = (By.CSS_SELECTOR, 'button > span.file-icon_dir_plus')
    #DISK_DIR_PLUS = (By.CSS_SELECTOR, '//div/button[1]/span[1]')
    DISK_DIR_PLUS = (By.CSS_SELECTOR, 'button.create-resource-popup-with-anchor__create-item > span.file-icon_dir_plus')
    DISK_FILE_PLUS = (By.CSS_SELECTOR, 'button.create-resource-popup-with-anchor__create-item > span.file-icon_doc')
    DISK_DIALOG = (By.CSS_SELECTOR, 'div.dialog__wrap')
    DISK_OBJ_NAME = (By.CSS_SELECTOR, 'form.rename-dialog__rename-form > span > input.Textinput-Control')
    DISK_SUBMIT_BTN = (By.CSS_SELECTOR, 'button.confirmation-dialog__button_submit')
    DISK_LISTING = (By.CSS_SELECTOR, 'div.listing_completed')
    #DISK_ITEMS = (By.CSS_SELECTOR, 'div.listing-item')
    DISK_ITEMS = (By.CSS_SELECTOR, 'div.listing-item_theme_tile')
    #DISK_ITEMS_TITLE = (By.CSS_SELECTOR, 'div.listing-item__title') # in same function
    #DISK_ITEMS_TITLE = (By.CSS_SELECTOR, 'div.listing-item__title > span[title="SDET_UI_Test_1"]')

    def get_DISK_ITEMS_TITLE_selector(self, name):
        #DISK_ITEMS_TITLE = (By.CSS_SELECTOR, f'div.listing-item__title > span[title="{name}"]')
        DISK_ITEMS_TITLE = (By.CSS_SELECTOR, f'div.listing-item__title[aria-label="{name}"]')
        # div.listing-item__title[aria-label="SDET_UI_Dir_1"]
        print(str(DISK_ITEMS_TITLE))
        return DISK_ITEMS_TITLE

