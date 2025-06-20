import random
import re
from pages.element_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            input_data = text_box_page.fill_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data, "The data doesn't match"

    class TestChechBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, "Checkboxes haven't been selected "

    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' has not been selected"
            assert output_impressive == 'Impressive', "'Impressive' has not been selected"
            assert output_no == 'No', "'No' has not been selected"

    class TestWebTables:

        def test_web_tables_add_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            new_person = web_tables_page.add_new_person()
            all_persons = web_tables_page.check_new_person()
            assert new_person in all_persons, "The person has not been added to the table"

        def test_web_tables_person_search(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            key_word = web_tables_page.add_new_person()[random.randint(0,5)]
            web_tables_page.search_person(key_word)
            table_result = web_tables_page.check_search_person()
            assert key_word in table_result, "The person has not been founded in the table"

        def test_web_tables_edit_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            last_name = web_tables_page.add_new_person()[1]
            web_tables_page.search_person(last_name)
            age = web_tables_page.update_person_info()
            row = web_tables_page.check_search_person()
            assert age in row, "The person has not been changed"

        def test_web_table_delete_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            email = web_tables_page.add_new_person()
            web_tables_page.search_person(email)
            web_tables_page.delete_person()
            text = web_tables_page.check_deleted()
            assert text == "No rows found"


