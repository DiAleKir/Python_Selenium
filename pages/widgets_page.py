from selenium.common import TimeoutException

from locators.widgets_locators import AccordianPageLocators
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