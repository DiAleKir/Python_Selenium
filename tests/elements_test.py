import random
import allure

from pages.element_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


@allure.suite("Elements")
class TestElements:

    @allure.feature('Text Box')
    class TestTextBox:

        @allure.title('Check Text Box')
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            input_data = text_box_page.fill_fields()
            output_data = text_box_page.check_filled_form()
            assert input_data == output_data, "The data doesn't match"


    @allure.feature('Check Box')
    class TestCheckBox:

        @allure.title('Check Check Box')
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, "Checkboxes haven't been selected "

    @allure.feature('Radio Button')
    class TestRadioButton:

        @allure.title('Check Radio Button')
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


    @allure.feature('Web Tables')
    class TestWebTables:

        @allure.title('Check adding a new person to the table')
        def test_web_tables_add_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            new_person = web_tables_page.add_new_person()
            all_persons = web_tables_page.check_new_person()
            assert new_person in all_persons, "The person has not been added to the table"

        @allure.title('Check the table search')
        def test_web_tables_person_search(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            key_word = web_tables_page.add_new_person()[random.randint(0,5)]
            web_tables_page.search_person(key_word)
            table_result = web_tables_page.check_search_person()
            assert key_word in table_result, "The person has not been founded in the table"

        @allure.title('Check for changes to person data')
        def test_web_tables_edit_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            last_name = web_tables_page.add_new_person()[1]
            web_tables_page.search_person(last_name)
            age = web_tables_page.update_person_info()
            row = web_tables_page.check_search_person()
            assert age in row, "The person has not been changed"

        @allure.title('Check the deletion of a person')
        def test_web_table_delete_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            email = web_tables_page.add_new_person()
            web_tables_page.search_person(email)
            web_tables_page.delete_person()
            text = web_tables_page.check_deleted()
            assert text == "No rows found"

        @allure.title('Check the change in the number of rows')
        def test_web_tables_change_count_row(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            count = web_tables_page.select_up_to_some_rows()
            assert count == [5,10,20,25,50,100], "The number of rows is not equal to the selected value"

    @allure.feature('Buttons')
    class TestButtonPage:

        @allure.title('Check the "double-click" button')
        def test_double_click_me_button(self, driver):
            button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            message =  button_page.click_double_click_me_button()
            assert message == "You have done a double click", "The button 'double click me' was not pressed"

        @allure.title('Check the "right-click" button')
        def test_right_click_me_button(self, driver):
            button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            message = button_page.click_right_click_me_button()
            assert message == "You have done a right click", "The button 'right click me' was not pressed"

        @allure.title('Check the "click me" button')
        def test_click_me_button(self, driver):
            button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            message = button_page.click_click_me_button()
            assert message == "You have done a dynamic click", "The button 'click me' was not pressed"

    @allure.feature('Links')
    class TestLinksPage:

        @allure.title('Check the link to the main page')
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "The link if broken or url is incorrect"

        @allure.title('Check the "create" link')
        def test_create_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_create_link('https://demoqa.com/created')
            assert response_code == 201, 'The link does not work or status code is non 201'

        @allure.title('Check the "bad request" link')
        def test_bad_request_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_create_link('https://demoqa.com/bad-request')
            assert response_code == 400, 'The link does not work or status code is non 400'

        @allure.title('Check the "forbidden" link')
        def test_forbidden_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_create_link('https://demoqa.com/forbidden')
            assert response_code == 403, 'The link does not work or status code is non 403'

        @allure.title('Check the "not found" link')
        def test_not_found_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_create_link('https://demoqa.com/invalid-url')
            assert response_code == 404, 'The link does not work or status code is non 404'

    @allure.feature('Upload and Download')
    class TestUploadAndDownload:

        @allure.title('Check the file upload')
        def test_upload_file(self, driver):
            up_and_down_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            up_and_down_page.open()
            file_name, result = up_and_down_page.upload_file()
            assert file_name == result, 'The file has not been uploaded'

        @allure.title('Check the file download')
        def test_download_file(self, driver):
            up_and_down_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            up_and_down_page.open()
            check = up_and_down_page.download_file()
            assert check is True, 'The file has not been download'

    @allure.feature('Dynamic Properties')
    class TestDynamicProperties:

        @allure.title('Check the clickability of the button after 5 seconds')
        def test_enable_after_5_seconds_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button_after_5_seconds()
            assert enable is True, "Button did not enable after 5 second"

        @allure.title('Check the button color change after 5 seconds')
        def test_color_change_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, colore_after = dynamic_properties_page.check_changed_of_color()
            assert color_before != colore_after, "Color have not been change"

        @allure.title('Check the button appearance after 5 seconds')
        def test_visible_after_5_seconds_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_button_after_5_seconds()
            assert appear is True, "Button did not appear after 5 second"

