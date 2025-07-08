import allure

from pages.form_page import FormPage


@allure.suite('Form')
@allure.feature('Form')
class TestForm:

    @allure.title('Check the completion of the Student Registration Form')
    def test_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        person = form_page.fill_form_fields()
        result = form_page.form_result()
        assert [person.first_name + " " + person.last_name, person.email] == [result[0], result[1]], \
            'The form has not been filled'
