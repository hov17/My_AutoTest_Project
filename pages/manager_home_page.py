import allure
from base.base_page import BasePage
from utilities.locators import ManagerHomePageLocators
from utilities.logger import Logger


class ManagerHomePage(BasePage):
    def go_to_add_customer_page(self):
        with allure.step('Go to add customer page'):
            Logger.add_start_step(method='go_to_add_customer_page')
            self.browser.find_element(*ManagerHomePageLocators.ADD_CUSTOMER_BUTTON).click()
            Logger.add_end_step(self.browser.current_url, method='go_to_add_customer_page')
