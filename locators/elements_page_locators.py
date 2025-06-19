from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    # form fields
    FULL_NAME = (By.XPATH, '//input[@id="userName"]')
    EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    PERMANENT_ADDRESS = (By.XPATH, '//textarea[@id="permanentAddress"]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')

    # created from
    CREATED_FULL_NAME = (By.XPATH, '//p[@id="name"]')
    CREATED_EMAIL = (By.XPATH, '//p[@id="email"]')
    CREATED_CURRENT_ADDRESS = (By.XPATH, '//p[@id="currentAddress"]')
    CREATED_PERMANENT_ADDRESS = (By.XPATH, '//p[@id="permanentAddress"]')


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.XPATH, '//button[@title="Expand all"]')
    ITEM_LIST = (By.XPATH, '//span[@class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = (By.XPATH, './/ancestor::span[@class = "rct-text"]')
    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')

class RadioButtonPageLocators:

    YES_BUTTON = (By.XPATH, '//label[@for="yesRadio"]')
    IMPRESSIVE_BUTTON = (By.XPATH, '//label[@for="impressiveRadio"]')
    NO_BUTTON = (By.XPATH, '//label[@for="noRadio"]')
    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')


class WebTablesPageLocators:

    ADD_BUTTON = (By.XPATH, '//button[@id="addNewRecordButton"]')
    FIRST_NAME = (By.XPATH, '//input[@id="firstName"]')
    LAST_NAME = (By.XPATH, '//input[@id="lastName"]')
    EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    AGE = (By.XPATH, '//input[@id="age"]')
    SALARY = (By.XPATH, '//input[@id="salary"]')
    DEPARTMENT = (By.XPATH, '//input[@id="department"]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')

