from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys("Sam")
        self.element_is_visible(self.locators.EMAIL).send_keys("Sam@serious.com")
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys("Leon")
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys("Leon")
        self.element_is_visible(self.locators.SUBMIT).click()
