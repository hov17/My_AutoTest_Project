import allure
from base.base_page import BasePage
from utilities.locators import AddCustomerPageLocators
from utilities.logger import Logger


class AddCustomerPage(BasePage):
    # Метод добавления нового пользователя
    def add_new_customer(self, first_name, last_name, code):
        with allure.step('Add new customer'):
            Logger.add_start_step(method='add_new_customer')
            self.browser.find_element(*AddCustomerPageLocators.FIRST_NAME_INPUT_FIELD).send_keys(first_name)
            self.browser.find_element(*AddCustomerPageLocators.LAST_NAME_INPUT_FIELD).send_keys(last_name)
            self.browser.find_element(*AddCustomerPageLocators.POST_CODE_INPUT_FIELD).\
                send_keys(code)
            self.browser.find_element(*AddCustomerPageLocators.ADD_CUSTOMER_BUTTON).click()
            assert self.browser.switch_to.alert.text == 'Customer added successfully with customer id :6', \
                'Wrong text message!'
            self.browser.switch_to.alert.accept()
            Logger.add_end_step(self.browser.current_url, method='add_new_customer')
