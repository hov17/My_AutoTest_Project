import allure
from pages.login_page import LoginPage
from pages.Customer.customer_authorization_page import CustomerAuthorizationPage


# Тест авторизации пользователя
@allure.description('Test customer authorization')
def test_customer_authorization(browser):
    url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    page = LoginPage(browser, url, timeout=10)
    page.open()
    page.customer_login_in_system()
    page = CustomerAuthorizationPage(browser, browser.current_url, timeout=10)
    page.customer_authorization('Harry Potter')
    page.is_url_address_correct('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account')
    page.get_screenshot()
