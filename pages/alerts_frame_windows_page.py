from locators.alerts_frame_windows_page_locators import BrowserWindowPageLocators
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    locators = BrowserWindowPageLocators()

    def check_opened_new_tab(self, key):
        if key == 'tab':
            self.element_is_clickable(self.locators.NEW_TAB_BUTTON).click()
            self.switch_window(1)
            text_title = self.element_is_present(self.locators.TITLE_NEW_TAB).text

        elif key == 'window':
            self.element_is_clickable(self.locators.NEW_WINDOW_BUTTON).click()
            self.switch_window(1)
            text_title = self.element_is_present(self.locators.TITLE_NEW_TAB).text

        return text_title