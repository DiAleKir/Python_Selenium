from pages.alerts_frame_windows_page import BrowserWindowPage, AlertsPage


class TestAlertsFrameWindows:

    class TestBrowserWindow:

        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab('tab')
            assert text_result == 'This is a sample page', 'The new tab has not opened'

        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab('window')
            assert text_result == 'This is a sample page', 'The new window has not opened'


    class TestAlerts:

        def test_see_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_see_alert()
            assert alert_text == 'You clicked a button', 'The alert did not show up'

        def test_appear_alert_after_5_sec(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_appear_alert_button()
            assert alert_text == 'This alert appeared after 5 seconds', 'The alert did not show up'

        def test_confirm_alert(self, driver):
            result_message = ['You selected Ok', 'You selected Cancel']
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_confirm_alert()
            assert alert_text in result_message, 'The alert did not show up'

        def test_prompt_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text, alert_message = alerts_page.check_prompt_alert()
            assert text in alert_message, 'The alert did not show up'