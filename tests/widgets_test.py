
from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage


class TestWidgets:

    class TestAccordian:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_text = accordian_page.check_accordian('first')
            second_title, second_text = accordian_page.check_accordian('second')
            third_title, third_text = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_text > 0, "Incorrect title or missing text"
            assert second_title == 'Where does it come from?' and second_text > 0,"Incorrect title or missing text"
            assert third_title == 'Why do we use it?' and third_text > 0,"Incorrect title or missing text"

    class TestAutoComplete:

        def test_fill_multi_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            count_of_colors = auto_complete_page.fill_input_multi()
            assert count_of_colors > 0, "No colors have been selected"

        def test_remove_value_from_multi_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            value_before, value_after = auto_complete_page.remove_value_from_multi_input()
            assert value_before > value_after, "The color has not been removed"

        def test_remove_all_value_from_multi_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            empty_multi_complete = auto_complete_page.remove_all_value_from_multi_input()
            assert empty_multi_complete is True, "The colors have not been removed"

        def test_fill_single_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color = auto_complete_page.fill_single_auto_complete()
            color_result = auto_complete_page.check_color_in_single_auto_complete()
            assert color == color_result, "The color have not been selected"

        
    class TestDatePicker:

        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date_before, date_after = date_picker_page.select_date()
            assert date_before != date_after, 'The date has not been changed'

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_day_and_time()
            assert value_date_before != value_date_after, 'The date and time has not been changed'


    class TestSlider:

        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            value_before, value_after = slider_page.change_slider_value()
            assert value_before != value_after