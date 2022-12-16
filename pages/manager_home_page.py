import allure
from base.base_page import BasePage
from utilities.locators import ManagerHomePageLocators
from utilities.logger import Logger


class ManagerHomePage(BasePage):
    # Метод для перехода на страницу добавления пользователя
    def go_to_add_customer_page(self):
        with allure.step('Go to add customer page'):
            Logger.add_start_step(method='go_to_add_customer_page')
            self.browser.find_element(*ManagerHomePageLocators.ADD_CUSTOMER_BUTTON).click()
            Logger.add_end_step(self.browser.current_url, method='go_to_add_customer_page')

    # Метод для перехода на страницу добавления нового счета
    def go_to_open_account_page(self):
        with allure.step('Go to open account page'):
            Logger.add_start_step(method='go_to_open_account_page')
            self.browser.find_element(*ManagerHomePageLocators.OPEN_ACCOUNT_BUTTON).click()
            Logger.add_end_step(self.browser.current_url, method='go_to_open_account_page')
