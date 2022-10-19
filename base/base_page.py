import datetime
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


# Класс с базовыми методами
class BasePage():
    # Конструктор - вызывается, когда мы создаем объект класса, то есть новую страницу
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Метод открывающий страницу браузера
    def open(self):
        with allure.step('Open browser'):
            Logger.add_start_step(method='open')
            self.browser.get(self.url)
            self.browser.maximize_window()
            Logger.add_end_step(self.browser.current_url, method='open')

    # Метод для получения скриншота страницы
    def get_screenshot(self):
        with allure.step('Get screenshot'):
            Logger.add_start_step(method='get_screenshot')
            name_screenshot = 'screenshot-' + str(datetime.datetime.utcnow().strftime("%d.%m.%Y.%H.%M.%S")) + '.png'
            self.browser.save_screenshot('C:\\Users\\Эмиль\\pythonProject\\My_AutoTest_Project\\screen\\'
                                         + name_screenshot)
            Logger.add_end_step(self.browser.current_url, method='get_screenshot')

    # Метод для проверки элемента на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # Метод для проверки того, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
