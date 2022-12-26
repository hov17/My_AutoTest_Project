import allure
from base.base_page import BasePage
from utilities.logger import Logger
from utilities.locators import LoginPageLocators


class LoginPage(BasePage):
    # Метод для авторизации в личный кабинет менеджера
    def manager_login_in_system(self):
        with allure.step('Manager login in system'):
            Logger.add_start_step(method='manager_login_in_system')
            self.browser.find_element(*LoginPageLocators.MANAGER_LOGIN_BUTTON).click()
            Logger.add_end_step(self.browser.current_url, method='manager_login_in_system')


    # Метод для авторизации в личный кабинет пользователя
    def customer_login_in_system(self):
        with allure.step('Customer login in system'):
            Logger.add_start_step(method='customer_login_in_system')
            self.browser.find_element(*LoginPageLocators.CUSTOMER_LOGIN_BUTTON).click()
            Logger.add_end_step(self.browser.current_url, method='customer_login_in_system')
