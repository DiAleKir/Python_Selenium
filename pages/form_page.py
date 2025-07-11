import os
import random

import allure
from selenium.webdriver import Keys
from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators

    @allure.step('Fill in all fields')
    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        subject_list = ['Hindi', 'English', 'Maths', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Commerce',
                        'Accounting', 'Economics', 'Arts', 'Social Studies', 'History', 'Civics']
        state_list = ['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']

        with allure.step('Fill in the full name field'):
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
        with allure.step('Fill in the last name field'):
            self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
        with allure.step('Fill in the email field'):
            self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        with allure.step('Fill in the gender field'):
            self.element_is_visible(self.locators.GENDER).click()
        with allure.step('Fill in the mobile field'):
            self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
        with allure.step('Fill in the subject field'):
            self.element_is_visible(self.locators.SUBJECT).send_keys(random.choice(subject_list))
            self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        with allure.step('Fill in the hobbies field'):
            self.element_is_visible(self.locators.HOBBIES).click()
        with allure.step('Upload an image'):
            self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(file_name)
        with allure.step('Fill in the current address field'):
            self.element_is_present(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        with allure.step('Fill in the state field'):
            self.element_is_present(self.locators.SELECT_STATE).click()
            self.element_is_present(self.locators.STATE_INPUT).send_keys(random.choice(state_list))
            self.element_is_present(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        with allure.step('Fill in the city field'):
            self.element_is_present(self.locators.SELECT_CITY).click()
            self.element_is_present(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        with allure.step('Click submit button'):
            self.element_is_clickable(self.locators.SUBMIT).click()
        return person

    @allure.step('Check the correct display of the filled fields')
    def form_result(self):
        result_list = self.elements_are_present(self.locators.RESULT_TABLE)
        data = []
        for _ in result_list:
            data.append(_.text)
        return data
