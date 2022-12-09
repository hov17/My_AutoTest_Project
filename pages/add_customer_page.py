import allure
import names
import random
from base.base_page import BasePage
from utilities.locators import AddCustomerPageLocators
from utilities.logger import Logger


class AddCustomerPage(BasePage):
    def add_new_customer(self):
        with allure.step('Add new customer'):
            Logger.add_start_step(method='add_new_customer')
            self.browser.find_element(*AddCustomerPageLocators.FIRST_NAME_INPUT_FIELD).send_keys(names.get_first_name())
            self.browser.find_element(*AddCustomerPageLocators.LAST_NAME_INPUT_FIELD).send_keys(names.get_last_name())
            self.browser.find_element(*AddCustomerPageLocators.POST_CODE_INPUT_FIELD).\
                send_keys(random.randint(100000, 999999))
            self.browser.find_element(*AddCustomerPageLocators.ADD_CUSTOMER_BUTTON).click()
            assert self.browser.switch_to.alert.text == 'Customer added successfully with customer id :6', \
                'Wrong text message!'
            self.browser.switch_to.alert.accept()


