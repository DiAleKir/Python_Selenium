import allure

from pages.alerts_frame_windows_page import BrowserWindowPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


@allure.suite("Alerts, Frames & Windows")
class TestAlertsFrameWindows:

    @allure.feature('Browser Window')
    class TestBrowserWindow:

        @allure.title('Check the opening of a new tab')
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab('tab')
            assert text_result == 'This is a sample page', 'The new tab has not opened'

        @allure.title('Check the opening of a new window')
        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab('window')
            assert text_result == 'This is a sample page', 'The new window has not opened'

    @allure.feature('Alerts')
    class TestAlerts:

        @allure.title('Check the alert appear')
        def test_see_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_see_alert()
            assert alert_text == 'You clicked a button', 'The alert did not show up'

        @allure.title('Check the alert appear after 5 seconds')
        def test_appear_alert_after_5_sec(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_appear_alert_button()
            assert alert_text == 'This alert appeared after 5 seconds', 'The alert did not show up'

        @allure.title('Check the confirm box appear')
        def test_confirm_alert(self, driver):
            result_message = ['You selected Ok', 'You selected Cancel']
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_confirm_alert()
            assert alert_text in result_message, 'The alert did not show up'

        @allure.title('Check the prompt box appear')
        def test_prompt_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text, alert_message = alerts_page.check_prompt_alert()
            assert text in alert_message, 'The alert did not show up'

    @allure.feature('Frames')
    class TestFrames:

        @allure.title('Check for two frame')
        def test_frames(self, driver):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()
            result_frame1 = frames_page.check_frames('frame1')
            result_frame2 = frames_page.check_frames('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
            assert result_frame2 == ['This is a sample page', '100px', '100px'], 'The frame does not exist'

    @allure.feature('Nested Frames')
    class TestNestedFrames:

        @allure.title('Check nested frames')
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frames_page.open()
            parent_text, child_text = nested_frames_page.check_nested_frames()
            assert parent_text == "Parent frame", 'Nested frame does not exist'
            assert child_text == 'Child Iframe', 'Nested frame does not exist'

    @allure.feature('Modal Dialogs')
    class TestModalDialogs:

        @allure.title('Check the small modal dialog appear')
        def test_small_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            title, text_message = modal_dialogs_page.check_small_modal_dialogs()
            assert title == 'Small Modal', 'The modal dialog has incorrect title or modal dialog does not appear'
            assert 'This is a small modal' in text_message, 'The modal dialog has incorrect text'

        @allure.title('Check the large modal dialog appear')
        def test_large_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            title, text_message = modal_dialogs_page.check_large_modal_dialogs()
            assert title == 'Large Modal', 'The modal dialog has incorrect title or modal dialog does not appear'
            assert 'Lorem Ipsum has been' in text_message, 'The modal dialog has incorrect text'
