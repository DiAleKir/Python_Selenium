class BrowserWindowPageLocators:

    NEW_TAB_BUTTON = ('xpath', '//button[@id="tabButton"]')
    TITLE_NEW_TAB = ('xpath', '//h1[@id="sampleHeading"]')
    NEW_WINDOW_BUTTON = ('xpath', '//button[@id="windowButton"]')


class AlertsPageLocators:

    SEE_ALERT_BUTTON = ('xpath', '//button[@id="alertButton"]')
    APPEAR_ALERT_AFTER_5_SEC_BUTTON = ('xpath', '//button[@id="timerAlertButton"]')
    CONFIRM_BOX_ALERT_BUTTON = ('xpath', '//button[@id="confirmButton"]')
    RESULT_CONFIRM = ('xpath', '//span[@id="confirmResult"]')
    PROMPT_BOX_ALERT_BUTTON = ('xpath', '//button[@id="promtButton"]')
    PROMPT_BOX_ALERT_RESULT = ('xpath', '//span[@id="promptResult"]')

class FramesPageLocators:

    FIRST_FRAME = ('xpath', '//iframe[@id="frame1"]')
    SECOND_FRAME = ('xpath', '//iframe[@id="frame2"]')
    TITLE_FRAME = ('xpath', '//h1[@id="sampleHeading"]')

class NestedFramesPageLocators:

    PARENT_FRAME = ('xpath', '//iframe[@id="frame1"]')
    PARENT_FRAME_TEXT = ('xpath', '//body')
    CHILD_FRAME = ('xpath', '//iframe[@srcdoc="<p>Child Iframe</p>"]')
    CHILD_FRAME_TEXT = ('xpath', '//p')


class ModalDialogsPageLocators:

    SMALL_MODAL_BUTTON = ('xpath', '//button[@id="showSmallModal"]')
    TITLE_SMALL_MODAL = ('xpath', '//div[@id="example-modal-sizes-title-sm"]')
    TEXT_FROM_SMALL_MODAL = ('xpath', '//div[@class="modal-body"]')
    SMALL_MODAL_BUTTON_CLOSE = ('xpath', '//button[@id="closeSmallModal"]')

    LARGE_MODAL_BUTTON = ('xpath', '//button[@id="showLargeModal"]')
    TITLE_LARGE_MODAL = ('xpath', '//div[@id="example-modal-sizes-title-lg"]')
    TEXT_FROM_LARGE_MODAL = ('xpath', '//div[@class="modal-body"]')
    LARGE_MODAL_BUTTON_CLOSE = ('xpath', '//button[@id="closeLargeModal"]')
