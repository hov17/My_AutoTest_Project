from selenium.webdriver.common.by import By


class LoginPageLocators():
    MANAGER_LOGIN_BUTTON = (By.XPATH, '//div[@class="center"][2]/button')


class ManagerHomePageLocators():
    ADD_CUSTOMER_BUTTON = (By.XPATH, '//button[@ng-class="btnClass1"]')


class AddCustomerPageLocators():
    FIRST_NAME_INPUT_FIELD = (By.XPATH, '//input[@ng-model="fName"]')
    LAST_NAME_INPUT_FIELD = (By.XPATH, '//input[@ng-model="lName"]')
    POST_CODE_INPUT_FIELD = (By.XPATH, '//input[@ng-model="postCd"]')
    ADD_CUSTOMER_BUTTON = (By.XPATH, '//button[@class="btn btn-default"]')
