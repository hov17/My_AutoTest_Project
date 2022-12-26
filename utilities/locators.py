from selenium.webdriver.common.by import By


class LoginPageLocators():
    MANAGER_LOGIN_BUTTON = (By.XPATH, '//div[@class="center"][2]/button')
    CUSTOMER_LOGIN_BUTTON = (By.XPATH, '//div[@class="center"][1]/button')


class ManagerHomePageLocators():
    ADD_CUSTOMER_BUTTON = (By.XPATH, '//button[@ng-class="btnClass1"]')
    OPEN_ACCOUNT_BUTTON = (By.XPATH, '//button[@ng-class="btnClass2"]')
    CUSTOMERS_BUTTON = (By.XPATH, '//button[@ng-class="btnClass3"]')


class AddCustomerPageLocators():
    FIRST_NAME_INPUT_FIELD = (By.XPATH, '//input[@ng-model="fName"]')
    LAST_NAME_INPUT_FIELD = (By.XPATH, '//input[@ng-model="lName"]')
    POST_CODE_INPUT_FIELD = (By.XPATH, '//input[@ng-model="postCd"]')
    ADD_CUSTOMER_BUTTON = (By.XPATH, '//button[@class="btn btn-default"]')


class OpenAccountPageLocators():
    CUSTOMER_DROPDOWN = (By.XPATH, '//select[@id="userSelect"]')
    USER_HARRY_POTTER = (By.XPATH, '//option[text()="Harry Potter"]')
    CURRENCY_DROPDOWN = (By.XPATH, '//select[@id="currency"]')
    POUND_CURRENCY = (By.XPATH, '//option[@value="Pound"]')
    PROCESS_BUTTON = (By.XPATH, '//button[@type="submit"]')


class CustomersPageLocators():
    SEARCHING_FIELD = (By.XPATH, '//input[@ng-model="searchCustomer"]')
    DELETE_CUSTOMER_BUTTON = (By.XPATH, '//button[@ng-click="deleteCust(cust)"]')


class CustomersAuthorizationPageLocators():
    CUSTOMERS_DROPDOWN = (By.XPATH, '//select[@id="userSelect"]')
    CUSTOMER_ALBUS_DUMBLEDORE = (By.XPATH, '//select[@id="userSelect"]/option[text()="Albus Dumbledore"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')

class CustomerAccountPageLocators():
    LOGOUT_BUTTON = (By.XPATH, '//button[@class="btn logout"]')
