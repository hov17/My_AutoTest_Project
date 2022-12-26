import allure
import names
import random
from pages.Manager.add_customer_page import AddCustomerPage
from pages.login_page import LoginPage
from pages.Manager.manager_home_page import ManagerHomePage
from pages.Manager.open_account_page import OpenAccountPage
from pages.Manager.customers_page import CustomersPage


# Тест авторизации менеджера в личный кабинет
@allure.description('Manager login test')
def test_manager_login(browser):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    page = LoginPage(browser, url, timeout=10)
    page.open()
    page.manager_login_in_system()
    page.is_url_address_correct('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager')
    page.get_screenshot()


# Тест добавления нового пользователя
@allure.description('Add new customer')
def test_add_new_customer(browser):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    page = LoginPage(browser, url, timeout=10)
    page.open()
    page.manager_login_in_system()
    page = ManagerHomePage(browser, browser.current_url, timeout=10)
    page.go_to_add_customer_page()
    page = AddCustomerPage(browser, browser.current_url)
    page.add_new_customer(names.get_first_name(), names.get_last_name(), random.randint(100000, 999999))


# Тест открытия нового счета для пользователя
@allure.description('Open new account for user')
def test_open_new_account_for_user(browser):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    page = LoginPage(browser, url, timeout=10)
    page.open()
    page.manager_login_in_system()
    page = ManagerHomePage(browser, browser.current_url, timeout=10)
    page.go_to_open_account_page()
    page = OpenAccountPage(browser, browser.current_url, timeout=10)
    page.open_new_account_for_customer()


# Тест удаления пользователя из списка
@allure.description('Delete user')
def test_delete_user(browser):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    page = LoginPage(browser, url, timeout=10)
    page.open()
    page.manager_login_in_system()
    page = ManagerHomePage(browser, browser.current_url, timeout=10)
    page.go_to_add_customer_page()
    page = AddCustomerPage(browser, browser.current_url, timeout=10)
    page.add_new_customer('test_name', 'test_surname', '123456')
    page = ManagerHomePage(browser, browser.current_url, timeout=10)
    page.go_to_customers_page()
    page = CustomersPage(browser, browser.current_url, timeout=10)
    page.delete_customer('test_name')
    page.get_screenshot()
