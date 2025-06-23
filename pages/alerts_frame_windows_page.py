import random
import time

from selenium.common import  NoAlertPresentException

from locators.alerts_frame_windows_page_locators import BrowserWindowPageLocators, AlertsPageLocators
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

class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_clickable(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window_text = alert_window.text
        alert_window.accept()
        return alert_window_text

    def check_appear_alert_button(self):
        self.element_is_clickable(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(5)
        try:
            alert_window= self.driver.switch_to.alert
            return alert_window.text
        except NoAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    def check_confirm_alert(self):
        confirm_choice = ['accept', 'dismiss']
        self.element_is_clickable(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_choice = random.choice(confirm_choice)
        if alert_choice == 'accept':
            alert_window.accept()
        else:
            alert_window.dismiss()
        text_result = self.element_is_present(self.locators.RESULT_CONFIRM).text
        return text_result

    def check_prompt_alert(self):
        text = f'test message {random.randint(1,50)}'
        self.element_is_clickable(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        alert_message = self.element_is_present(self.locators.PROMPT_BOX_ALERT_RESULT).text
        return text, alert_message
