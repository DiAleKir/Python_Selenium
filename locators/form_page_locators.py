import random

from selenium.webdriver.common.by import By


class FormPageLocators:
    # form fields
    FIRST_NAME = (By.XPATH, '//input[@id="firstName"]')
    LAST_NAME = (By.XPATH, '//input[@id="lastName"]')
    EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    GENDER = (By.XPATH, f'//label[contains(@for, "gender-radio-{random.randint(1, 3)}")]')
    MOBILE = (By.XPATH, '//input[@id="userNumber"]')
    DATA_OF_BIRTH = (By.XPATH, '//input[@id="dateofBirthInput"]')
    SUBJECT = (By.XPATH, '//input[@id="subjectsInput"]')
    HOBBIES = (By.XPATH, f'//label[contains(@for, "hobbies-checkbox-{random.randint(1, 3)}")]')
    FILE_INPUT = (By.XPATH, '//input[@id="uploadPicture"]')
    CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    SELECT_STATE = (By.XPATH, '//div[@id="state"]')
    STATE_INPUT = (By.XPATH, '//div[@id="state"]//input[contains(@id, "react-select")]')
    SELECT_CITY = (By.XPATH, '//div[@id="city"]')
    CITY_INPUT = (By.XPATH, '//div[@id="city"]//input[contains(@id, "react-select")]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')

    # table result
    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
