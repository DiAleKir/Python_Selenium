

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