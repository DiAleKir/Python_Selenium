import base64
import os
import random

import allure
import requests

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablesPageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadPageLocators, \
    DynamicPropertiesPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step('Fill in all fields')
    def fill_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        with allure.step('Filling in the full name field'):
            self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        with allure.step('Filling in the email field'):
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
        with allure.step('Filling in the current address field'):
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        with allure.step('Filling in the permanent address field'):
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        with allure.step('Click the submit button'):
            self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    @allure.step('Check the correct display of the filled fields')
    def check_filled_form(self):
        with allure.step('Check the full name field'):
            full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        with allure.step('Check the email field'):
            email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[1]
        with allure.step('Check the current address field'):
            current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        with allure.step('Check the permanent address field'):
            permanent_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step('Open the full list of all checkboxes')
    def open_full_list(self):
        self.element_is_clickable(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step('Choose random checkboxes')
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1,15)]
            if count > 0:
                self.scroll_to_element(item)
                item.click()
                count -= 1
            else:
                break

    @allure.step('Check if the checkboxes are checked')
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, './/ancestor::span[@class = "rct-text"]')
            data.append(title_item.text)
        return str(data).replace(" ", "").replace(".doc", "").lower()

    @allure.step('Check the appearance of the names of the selected checkboxes under the list of all checkboxes')
    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(" ", "").lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step('Check all radio buttons')
    def click_on_radio_button(self, choice):
        choices = {'yes': self.locators.YES_BUTTON,
                  'impressive': self.locators.IMPRESSIVE_BUTTON,
                  'no': self.locators.NO_BUTTON}
        self.element_is_clickable(choices[choice]).click()

    @allure.step('Check the appearance of the names of the selected radio button under the list of radio button')
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text

class WebTablesPage(BasePage):
    locators = WebTablesPageLocators()

    @allure.step('Аdding a new person')
    def add_new_person(self, count=1):
        while count != 0:
            person_info = next(generated_person())
            first_name =person_info.first_name
            last_name =person_info.last_name
            email =person_info.email
            age =person_info.age
            salary =person_info.salary
            department =person_info.department
            with allure.step('Click Add button'):
                self.element_is_visible(self.locators.ADD_BUTTON).click()
            with allure.step('Filling in the first name field'):
                self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
            with allure.step('Filling in the last name field'):
                self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
            with allure.step('Filling in the email field'):
                self.element_is_visible(self.locators.EMAIL).send_keys(email)
            with allure.step('Filling in the age field'):
                self.element_is_visible(self.locators.AGE).send_keys(age)
            with allure.step('Filling in the salary field'):
                self.element_is_visible(self.locators.SALARY).send_keys(salary)
            with allure.step('Filling in the department field'):
                self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
            with allure.step('Click submit button'):
                self.element_is_visible(self.locators.SUBMIT).click()
            count -=1
            return [first_name, last_name, str(age), email , str(salary), department]

    @allure.step('Check the correct display of the filled fields')
    def check_new_person(self):
        persons_list = self.elements_are_present(self.locators.PERSONS_LIST)
        data = []
        for person in persons_list:
            data.append(person.text.splitlines())
        return data

    @allure.step('Search for a person using search input')
    def search_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.step('Check the search result')
    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, './/ancestor::div[@class="rt-tr-group"]')
        return row.text.splitlines()

    @allure.step('Update person information')
    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    @allure.step('Delete a person')
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step('Check the user\'s deletion')
    def check_deleted(self):
        return self.element_is_visible(self.locators.NO_ROWS_FOUND).text

    @allure.step('Change the number of rows in the table')
    def select_up_to_some_rows(self):
        count = [5,10,20,25,50,100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.ROWS_PER_PAGE)
            Select(count_row_button).select_by_value(str(x))
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.PERSONS_LIST)
        return len(list_rows)


class ButtonPage(BasePage):
    locators = ButtonsPageLocators()

    def click_double_click_me_button(self):
        self.double_click(self.element_is_clickable(self.locators.DOUBLE_CLICK_ME_BUTTON))
        return self.check_click_result(self.locators.DOUBLE_CLICK_ME_MESSAGE)

    def click_right_click_me_button(self):
        self.right_click(self.element_is_clickable(self.locators.RIGHT_CLICK_ME_BUTTON))
        return self.check_click_result(self.locators.RIGHT_CLICK_ME_MESSAGE)

    def click_click_me_button(self):
        self.element_is_clickable(self.locators.CLICK_ME_BUTTON).click()
        return self.check_click_result(self.locators.CLICK_ME_MESSAGE)

    @allure.step('Check the message appearance after clicking the button')
    def check_click_result(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = LinksPageLocators

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_clickable(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def check_create_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_clickable(self.locators.CREATED_LINK).click()
        else:
            return request.status_code

    def check_bad_request_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            return self.element_is_clickable(self.locators.BAD_REQUEST_LINK).click()
        else:
            return request.status_code


    def check_forbidden_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            return self.element_is_clickable(self.locators.FORBIDDEN_LINK).click()
        else:
            return request.status_code

    def check_not_found_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            return self.element_is_clickable(self.locators.NOT_FOUND_LINK).click()
        else:
            return request.status_code


class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_clickable(self.locators.UPLOAD_BUTTON).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOADED_RESULT).text
        return file_name.split('\\')[-1], text.split('\\')[-1]

    def download_file(self):
        link = self.element_is_clickable(self.locators.DOWNLOAD_BUTTON).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf'C:\PythonProject\PythonSelenium\test_img{random.randint(1,100)}.jpeg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators

    def check_enable_button_after_5_seconds(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_AFTER_BUTTON)
        except TimeoutException:
            return False
        return True

    def check_changed_of_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        self.wait_the_attribute_of_element_to_change(self.locators.COLOR_CHANGE_BUTTON, 'text-danger')
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    def check_appear_button_after_5_seconds(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_BUTTON)
        except TimeoutException:
            return False
        return True