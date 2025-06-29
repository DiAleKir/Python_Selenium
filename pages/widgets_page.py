import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

from generator.generator import generated_date
from locators.widgets_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, ToolTipsPageLocators, MenuPageLocators
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


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before =input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_from_list(self.locators.DATE_SELECT_DAY, date.day)
        value_date_after = input_date
        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_from_list(self, element, value):
        item_list = self.elements_are_present(element)
        for item in item_list:
            if item.text == value:
                item.click()
                break

    def select_day_and_time(self):
        date = next(generated_date())
        input_day_and_time = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_day_and_time.get_attribute('value')
        input_day_and_time.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
        self.set_date_from_list(self.locators.DATE_AND_TIME_DAY, date.day)
        self.set_date_from_list(self.locators.DATE_AND_TIME_TIME, date.time)
        value_date_after = input_day_and_time.get_attribute('value')
        return value_date_before, value_date_after

class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.VALUE_SLIDER).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.slide_action(slider_input, random.randint(1,100), 0)
        value_after = self.element_is_visible(self.locators.VALUE_SLIDER).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators

    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_INFO).text
        progress_bar_button = self.element_is_visible(self.locators.START_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(1,5))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_INFO).text
        return value_before, value_after


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_text_from_tool_tips(self, locator):
        hover = self.element_is_visible(locator)
        self.move_to_element(hover)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIP)
        text = tool_tip_text.text
        return text

    def check_tool_tips(self, hover_name):
        if hover_name == 'button':
            tool_tip = self.get_text_from_tool_tips(self.locators.BUTTON_WITH_HOVER)
        elif hover_name == 'text-field':
            tool_tip = self.get_text_from_tool_tips(self.locators.TEXT_FIELD_WITH_HOVER)
        elif hover_name == 'contrary':
            tool_tip= self.get_text_from_tool_tips(self.locators.CONTRARY_LINK)
        elif hover_name == 'section':
            tool_tip= self.get_text_from_tool_tips(self.locators.SECTION_LINK)
        return tool_tip


class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.move_to_element(item)
            data.append(item.text)
        return data