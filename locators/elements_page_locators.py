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

    #Add person form
    ADD_BUTTON = (By.XPATH, '//button[@id="addNewRecordButton"]')
    FIRST_NAME = (By.XPATH, '//input[@id="firstName"]')
    LAST_NAME = (By.XPATH, '//input[@id="lastName"]')
    AGE = (By.XPATH, '//input[@id="age"]')
    EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    SALARY = (By.XPATH, '//input[@id="salary"]')
    DEPARTMENT = (By.XPATH, '//input[@id="department"]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')

    #tables
    PERSONS_LIST = (By.XPATH, '//div[@class="rt-tr-group"]')
    SEARCH_INPUT = (By.XPATH, '//input[@id="searchBox"]')
    DELETE_BUTTON = (By.XPATH, '//span[@title="Delete"]')
    UPDATE_BUTTON = (By.XPATH, '//span[@title="Edit"]')
    NO_ROWS_FOUND = (By.XPATH, '//div[@class="rt-noData"]')
    ROWS_PER_PAGE = (By.XPATH, '//select[@aria-label="rows per page"]')

class ButtonsPageLocators:

    DOUBLE_CLICK_ME_BUTTON = (By.XPATH, '//button[@id="doubleClickBtn"]')
    RIGHT_CLICK_ME_BUTTON = (By.XPATH, '//button[@id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By.XPATH, '//button[text()="Click Me"]')
    DOUBLE_CLICK_ME_MESSAGE = (By.XPATH, '//p[@id="doubleClickMessage"]')
    RIGHT_CLICK_ME_MESSAGE = (By.XPATH, '//p[@id="rightClickMessage"]')
    CLICK_ME_MESSAGE = (By.XPATH, '//p[@id="dynamicClickMessage"]')


class LinksPageLocators:

    SIMPLE_LINK = (By.XPATH, '//a[@id="simpleLink"]')
    CREATED_LINK = (By.XPATH, '//a[@id="created"]')
    BAD_REQUEST_LINK = (By.XPATH, '//a[@id="bad-request"]')
    FORBIDDEN_LINK = (By.XPATH, '//a[@id="forbidden"]')
    NOT_FOUND_LINK = (By.XPATH, '//a[@id="invalid-url"]')


class UploadAndDownloadPageLocators:

    UPLOAD_BUTTON = (By.XPATH, '//input[@id="uploadFile"]')
    UPLOADED_RESULT = (By.XPATH, '//p[@id="uploadedFilePath"]')
    DOWNLOAD_BUTTON = (By.XPATH, '//a[@id="downloadButton"]')




