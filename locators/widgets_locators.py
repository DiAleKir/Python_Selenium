

class AccordianPageLocators:

    FIRST_SECTION = ('xpath', '//div[@id="section1Heading"]')
    FIRST_SECTION_TEXT = ('xpath', '//div[@id="section1Content"]/p')
    SECOND_SECTION = ('xpath', '//div[@id="section2Heading"]')
    SECOND_SECTION_TEXT = ('xpath', '//div[@id="section2Content"]/p')
    THIRD_SECTION = ('xpath', '//div[@id="section3Heading"]')
    THIRD_SECTION_TEXT = ('xpath', '//div[@id="section3Content"]/p')


class AutoCompletePageLocators:
    MULTI_COMPLETE = ('xpath', '//input[@id="autoCompleteMultipleInput"]')
    MULTI_VALUE = ('xpath', '//div[@class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = ('xpath', '//div[contains(@class, "css-xb97g8")]//*[name()="path"]')
    MULTI_REMOVE_ALL = ('xpath', '//div[contains(@class, "auto-complete__clear-indicator")]//*[name()="path"]')
    SINGLE_VALUE = ('xpath', '//div[@class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = ('xpath', '//input[@id="autoCompleteSingleInput"]')


class DatePickerPageLocators:

    DATE_INPUT = ('xpath', '//input[@id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = ('xpath', '//select[@class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = ('xpath', '//select[@class="react-datepicker__year-select"]')
    DATE_SELECT_DAY = ('xpath', '//div[contains(@class, "react-datepicker__day--")]')

    DATE_AND_TIME_INPUT = ('xpath', '//input[@id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH = ('xpath', '//span[@class="react-datepicker__month-read-view--selected-month"]')
    DATE_AND_TIME_MONTH_LIST = ('xpath', '//div[@class="react-datepicker__month-option"]')
    DATE_AND_TIME_YEAR = ('xpath', '//span[@class="react-datepicker__year-read-view--selected-year"]')
    DATE_AND_TIME_YEAR_LIST = ('xpath', '//div[@class="react-datepicker__year-option"]')
    DATE_AND_TIME_DAY = ('xpath', '//div[contains(@class , "react-datepicker__day react-date")]')
    DATE_AND_TIME_TIME = ('xpath', '//li[@class="react-datepicker__time-list-item "]')


class SliderPageLocators:

    INPUT_SLIDER = ('xpath', '//input[@class="range-slider range-slider--primary"]')
    VALUE_SLIDER = ('xpath', '//input[@id="sliderValue"]')

class ProgressBarPageLocators:

    START_BUTTON = ('xpath', '//button[@id="startStopButton"]')
    PROGRESS_BAR_INFO  = ('xpath', '//div[@class="progress-bar bg-info"]')