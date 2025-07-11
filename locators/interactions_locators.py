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


class ResizablePageLocators:

    RESIZABLE_BOX = ('xpath', '//div[@id="resizableBoxWithRestriction"]')
    RESIZABLE_BOX_HANDLE = ('xpath', '//div[@id="resizableBoxWithRestriction"]//span')
    RESIZABLE = ('xpath', '//div[@id="resizable"]')
    RESIZABLE_HANDLE = ('xpath', '//div[@id="resizable"]//span')


class DroppablePageLocators:

    SIMPLE_TAB = ('xpath', '//a[@id="droppableExample-tab-simple"]')
    SIMPLE_TAB_DRAGGABLE = ('xpath', '//div[@id="draggable"]')
    SIMPLE_TAB_DROPPABLE = ('xpath', '//div[@id="simpleDropContainer"]//div[@id="droppable"]')

    ACCEPT_TAB = ('xpath', '//a[@id="droppableExample-tab-accept"]')
    ACCEPT_TAB_ACCEPTABLE = ('xpath', '//div[@id="acceptable"]')
    ACCEPT_TAB_NOT_ACCEPTABLE = ('xpath', '//div[@id="notAcceptable"]')
    ACCEPT_TAB_DROPPABLE = ('xpath', '//div[@id="droppableExample-tabpane-accept"]//div[@id="droppable"]')

    PREVENT_PROPOGATION_TAB = ('xpath', '//a[@id="droppableExample-tab-preventPropogation"]')
    DRAG_ME = ('xpath', '//div[@id="dragBox"]')
    NOT_GREEDY_DROP_BOX_TEXT = ('xpath', '//div[@id="notGreedyDropBox"]/p')
    NOT_GREEDY_DROP_INNER_BOX = ('xpath', '//div[@id="notGreedyInnerDropBox"]')
    NOT_GREEDY_DROP_INNER_BOX_TEXT = ('xpath', '//div[@id="notGreedyInnerDropBox"]/p')
    GREEDY_DROP_BOX_TEXT = ('xpath', '//div[@id="greedyDropBox"]/p')
    GREEDY_DROP_INNER_BOX = ('xpath', '//div[@id="greedyDropBoxInner"]')
    GREEDY_DROP_INNER_BOX_TEXT = ('xpath', '//div[@id="greedyDropBoxInner"]/p')

    REVENT_DRAGGABLE_TAB = ('xpath', '//a[@id="droppableExample-tab-revertable"]')
    WILL_REVERT = ('xpath', '//div[@id="revertable"]')
    NOT_REVERT = ('xpath', '//div[@id="notRevertable"]')
    DROP_HERE = ('xpath', '//div[@id="revertableDropContainer"]//div[@id="droppable"]')
