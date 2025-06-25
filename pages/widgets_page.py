import random
from itertools import count

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from locators.widgets_locators import AccordianPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':
                         {'title': self.locators.FIRST_SECTION,
                          'text': self.locators.FIRST_SECTION_TEXT},
                     'second':
                         {'title': self.locators.SECOND_SECTION,
                          'text': self.locators.SECOND_SECTION_TEXT},
                     'third':
                         {'title': self.locators.THIRD_SECTION,
                          'text': self.locators.THIRD_SECTION_TEXT}
                     }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_text = self.element_is_visible(accordian[accordian_num]['text']).text
        except TimeoutException:
            section_title.click()
            section_text = self.element_is_visible(accordian[accordian_num]['text']).text
        return [section_title.text, len(section_text)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()
    colors = ['Blue', 'Black', 'Aqua', 'Yellow', 'White', 'Red', 'Green', 'Purple']

    def fill_input_multi(self):
        color = random.sample(self.colors, k=random.randint(2,4))
        for c in color:
            input_multi = self.element_is_clickable(self.locators.MULTI_COMPLETE)
            input_multi.send_keys(c)
            input_multi.send_keys(Keys.ENTER)
        count_of_colors = len(self.elements_are_visible(self.locators.MULTI_COMPLETE))
        return count_of_colors

    def remove_value_from_multi_input(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def remove_all_value_from_multi_input(self):
        self.element_is_not_visible(self.locators.MULTI_VALUE)
        self.fill_input_multi()
        self.element_is_visible(self.locators.MULTI_VALUE)
        self.element_is_visible(self.locators.MULTI_REMOVE_ALL).click()
        empty_multi_input = self.element_is_not_visible(self.locators.MULTI_VALUE)
        return empty_multi_input

    def fill_single_auto_complete(self):
        color = random.sample(self.colors, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single_auto_complete(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text

