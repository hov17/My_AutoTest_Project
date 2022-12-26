import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utilities.locators import CustomersAuthorizationPageLocators
from utilities.locators import CustomerAccountPageLocators
from utilities.logger import Logger


class CustomerSelectionPage(BasePage):
    # Метод выбора пользователя
    def customer_authorization(self, customer_name):
        with allure.step('Customer authorization'):
            Logger.add_start_step(method='customer_authorization')
            self.browser.find_element(*CustomersAuthorizationPageLocators.CUSTOMERS_DROPDOWN).click()
            self.browser.find_element(By.XPATH, f'//select[@id="userSelect"]/option[text()="{customer_name}"]').click()
            self.browser.find_element(*CustomersAuthorizationPageLocators.LOGIN_BUTTON).click()
            assert self.browser.find_element(By.XPATH, f'//span[@class="fontBig ng-binding"]').text == customer_name,\
                'Wrong customer name!'
            assert self.is_element_present(*CustomerAccountPageLocators.LOGOUT_BUTTON)
            Logger.add_end_step(self.browser.current_url, method='customer_authorization')
