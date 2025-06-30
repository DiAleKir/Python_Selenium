class SortablePageLocators:

    TAB_LIST = ('xpath', '//a[@id="demo-tab-list"]')
    ITEM_LIST = ('xpath', '//div[@class="vertical-list-container mt-4"]/div')
    TAB_GRID = ('xpath', '//a[@id="demo-tab-grid"]')
    ITEM_GRID = ('xpath', '//div[@class="create-grid"]/div')


class SelectablePageLocators:

    TAB_LIST = ('xpath', '//a[@id="demo-tab-list"]')
    ITEM_LIST = ('xpath', '//div[@id="demo-tabpane-list"]//li')
    ITEM_LIST_ACTIVE = ('xpath', '//div[@id="demo-tabpane-list"]//li[contains(@class, "active")]')
    TAB_GRID = ('xpath', '//a[@id="demo-tab-grid"]')
    ITEM_GRID = ('xpath', '//div[@id="gridContainer"]//li')
    ITEM_GRID_ACTIVE = ('xpath', '//div[@id="gridContainer"]//li[contains(@class, "active")]')