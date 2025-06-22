import os
import random

from selenium.webdriver import Keys
from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        subject_list = ['Hindi', 'English', 'Maths', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Commerce',
                        'Accounting', 'Economics', 'Arts', 'Social Studies', 'History', 'Civics']
        state_list = ['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']

        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
        # self.element_is_visible(self.locators.DATA_OF_BIRTH).send_keys(person.first_name)
        self.element_is_visible(self.locators.SUBJECT).send_keys(random.choice(subject_list))
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(file_name)
        self.element_is_present(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_present(self.locators.SELECT_STATE).click()
        self.element_is_present(self.locators.STATE_INPUT).send_keys(random.choice(state_list))
        self.element_is_present(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_present(self.locators.SELECT_CITY).click()
        self.element_is_present(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_clickable(self.locators.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.elements_are_present(self.locators.RESULT_TABLE)
        data = []
        for _ in result_list:
            data.append(_.text)
        return data
