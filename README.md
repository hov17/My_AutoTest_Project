# My_AutoTest_Project
Мой тестовый проект по автоматизации тестирования. 
Используемый сайт - https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login

Локаторы для элементов находятся в папке utilities, файл locators.py

Файл pytest.ini нужен для хранения маркировок тестов

Дополнительно подключил логирование(файл в папке utilities) и отчеты с помощью Allure

Для получения отчета с логами в файле logger.py нужно указать путь к проекту

Папка с Allure добавлена в системный Path Для записи отчета Allure необходимо использовать параметр --alluredir="название папки для отчетов". Для чтения результатов прописать в консоли команду allure serve "название папки для отчетов".
