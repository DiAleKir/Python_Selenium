from pages.widgets_page import AccordianPage


class TestWidgets:

    class TestAccordian:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_text = accordian_page.check_accordian('first')
            second_title, second_text = accordian_page.check_accordian('second')
            third_title, third_text = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_text > 0
            assert second_title == 'Where does it come from?' and second_text > 0
            assert third_title == 'Why do we use it?' and third_text > 0
