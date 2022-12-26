import allure
from base.base_page import BasePage
from utilities.locators import CustomersPageLocators
from utilities.logger import Logger


class CustomersPage(BasePage):
    # Метод для удаления пользователя
    def delete_customer(self, first_name):
        with allure.step('Delete user'):
            Logger.add_start_step('delete_user')
            self.browser.find_element(*CustomersPageLocators.SEARCHING_FIELD).send_keys(first_name)
            self.browser.find_element(*CustomersPageLocators.DELETE_CUSTOMER_BUTTON).click()
            Logger.add_end_step(self.browser.current_url, method='delete_user')
