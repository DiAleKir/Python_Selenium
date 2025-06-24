import random
import time

from selenium.common import  NoAlertPresentException

from locators.alerts_frame_windows_page_locators import BrowserWindowPageLocators, AlertsPageLocators, \
    FramesPageLocators, NestedFramesPageLocators, ModalDialogsPageLocators
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

class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frames(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text , width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_nested_frames(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    def check_small_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        text = self.element_is_visible(self.locators.TEXT_FROM_SMALL_MODAL).text
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON_CLOSE).click()
        return title, text

    def check_large_modal_dialogs(self):
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        title = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        text_message = self.element_is_visible(self.locators.TEXT_FROM_LARGE_MODAL).text
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON_CLOSE).click()
        return title, text_message