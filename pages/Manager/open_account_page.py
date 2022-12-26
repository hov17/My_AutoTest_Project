import allure
from base.base_page import BasePage
from utilities.logger import Logger
from utilities.locators import OpenAccountPageLocators


class OpenAccountPage(BasePage):
    # Метод для открытия нового счета
    def open_new_account_for_customer(self):
        with allure.step('Open new account'):
            Logger.add_start_step(method='open_new_account_for_user')
            self.browser.find_element(*OpenAccountPageLocators.CUSTOMER_DROPDOWN).click()
            self.browser.find_element(*OpenAccountPageLocators.USER_HARRY_POTTER).click()
            self.browser.find_element(*OpenAccountPageLocators.CURRENCY_DROPDOWN).click()
            self.browser.find_element(*OpenAccountPageLocators.POUND_CURRENCY).click()
            self.browser.find_element(*OpenAccountPageLocators.PROCESS_BUTTON).click()
            assert self.browser.switch_to.alert.text == 'Account created successfully with account Number :1016',\
                'Wrong text message!'
            self.browser.switch_to.alert.accept()
            Logger.add_end_step(self.browser.current_url, method='open_new_account_for_user')
