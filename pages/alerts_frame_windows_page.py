import random
import time

import allure
from selenium.common import NoAlertPresentException

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

    @allure.step('Check for the alert after 5 seconds')
    def check_appear_alert_button(self):
        with allure.step('Click alert button'):
            self.element_is_clickable(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        with allure.step('Wait 5 seconds'):
            time.sleep(5)
        with allure.step('Switching to the alert and receiving the text from it'):
            try:
                alert_window = self.driver.switch_to.alert
                return alert_window.text
            except NoAlertPresentException:
                alert_window = self.driver.switch_to.alert
                return alert_window.text

    @allure.step('Check confirm box alert')
    def check_confirm_alert(self):
        confirm_choice = ['accept', 'dismiss']
        with allure.step('Click confirm box alert button'):
            self.element_is_clickable(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        with allure.step('Switching to the alert'):
            alert_window = self.driver.switch_to.alert
        with allure.step('Make a choice'):
            alert_choice = random.choice(confirm_choice)
        with allure.step('Check the appearance of the text after clicking the button according to the selection made'):
            if alert_choice == 'accept':
                alert_window.accept()
            else:
                alert_window.dismiss()
        text_result = self.element_is_present(self.locators.RESULT_CONFIRM).text
        return text_result

    @allure.step('Check prompt alert')
    def check_prompt_alert(self):
        text = f'test message {random.randint(1, 50)}'
        with allure.step('Click prompt alert'):
            self.element_is_clickable(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        with allure.step('Switching to the alert'):
            alert_window = self.driver.switch_to.alert
        with allure.step('Enter a name in the prompt box input field and click the OK button'):
            alert_window.send_keys(text)
            alert_window.accept()
        with allure.step('Check the appearance of the text after clicking the OK button'):
            alert_message = self.element_is_present(self.locators.PROMPT_BOX_ALERT_RESULT).text
        return text, alert_message


class FramesPage(BasePage):
    locators = FramesPageLocators()

    @allure.step('Check the frames')
    def check_frames(self, frame_num):
        with allure.step('Check the first frame'):
            if frame_num == 'frame1':
                with allure.step('Check attributes of the first frame'):
                    frame = self.element_is_present(self.locators.FIRST_FRAME)
                    width = frame.get_attribute('width')
                    height = frame.get_attribute('height')
                with allure.step('Switching to the second frame'):
                    self.driver.switch_to.frame(frame)
                with allure.step('Check title from the first frame'):
                    text = self.element_is_present(self.locators.TITLE_FRAME).text
                with allure.step('Switching to he main page'):
                    self.driver.switch_to.default_content()
                return [text, width, height]
        with allure.step('Check the second frame'):
            if frame_num == 'frame2':
                with allure.step('Check attributes of the second frame'):
                    frame = self.element_is_present(self.locators.SECOND_FRAME)
                    width = frame.get_attribute('width')
                    height = frame.get_attribute('height')
                with allure.step('Switching to the second frame'):
                    self.driver.switch_to.frame(frame)
                with allure.step('Check title from the first frame'):
                    text = self.element_is_present(self.locators.TITLE_FRAME).text
                with allure.step('Switching to he main page'):
                    self.driver.switch_to.default_content()
                return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    @allure.step('Check the nested frames')
    def check_nested_frames(self):
        with allure.step('Switching to the parent frame'):
            parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
            self.driver.switch_to.frame(parent_frame)
        with allure.step('Check text from the first frame'):
            parent_text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text
        with allure.step('Switching to the child frame'):
            child_frame = self.element_is_present(self.locators.CHILD_FRAME)
            self.driver.switch_to.frame(child_frame)
        with allure.step('Check text from the first frame'):
            child_text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    @allure.step('Check the small modal dialog')
    def check_small_modal_dialogs(self):
        with allure.step('Click the small modal button'):
            self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        with allure.step('Check title from the small modal'):
            title = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        with allure.step('Check title from the small modal'):
            text = self.element_is_visible(self.locators.TEXT_FROM_SMALL_MODAL).text
        with allure.step('Click close button'):
            self.element_is_visible(self.locators.SMALL_MODAL_BUTTON_CLOSE).click()
        return title, text

    @allure.step('Check the large modal dialog')
    def check_large_modal_dialogs(self):
        with allure.step('Click the large modal button'):
            self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        with allure.step('Check title from the large modal'):
            title = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        with allure.step('Check title from the large modal'):
            text_message = self.element_is_visible(self.locators.TEXT_FROM_LARGE_MODAL).text
        with allure.step('Click close button'):
            self.element_is_visible(self.locators.LARGE_MODAL_BUTTON_CLOSE).click()
        return title, text_message
