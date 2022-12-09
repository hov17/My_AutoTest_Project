import allure
import time
from pages.add_customer_page import AddCustomerPage
from pages.login_page import LoginPage
from pages.manager_home_page import ManagerHomePage


# Тест авторизации менеджера в личный кабинет
@allure.description('Manager login test')
def test_manager_login(browser):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    page = LoginPage(browser, url, timeout=10)
    page.open()
    page.manager_login_in_system()
    page.is_url_address_correct('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager')
    page.get_screenshot()


@allure.description('Add new customer')
def test_add_new_customer(browser):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    page = LoginPage(browser, url, timeout=10)
    page.open()
    page.manager_login_in_system()
    page = ManagerHomePage(browser, browser.current_url, timeout=10)
    page.go_to_add_customer_page()
    page = AddCustomerPage(browser, browser.current_url)
    page.add_new_customer()
