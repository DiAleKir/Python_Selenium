import random
import time

from locators.interactions_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, element):
        items_list = self.elements_are_visible(element)
        return [item.text for item in items_list]

    def change_list_order(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_items(self.locators.ITEM_LIST)
        item_list = random.sample(self.elements_are_visible(self.locators.ITEM_LIST), k=2)
        self.drag_and_drop(item_list[0], item_list[1])
        order_after = self.get_sortable_items(self.locators.ITEM_LIST)
        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_sortable_items(self.locators.ITEM_GRID)
        item_grid = random.sample(self.elements_are_visible(self.locators.ITEM_GRID), k=2)
        self.drag_and_drop(item_grid[0], item_grid[1])
        order_after = self.get_sortable_items(self.locators.ITEM_GRID)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        items = random.sample(item_list, k=2)
        for _ in items:
            _.click()

    def select_item(self, tab):
        if tab == 'list':
            self.element_is_visible(self.locators.TAB_LIST).click()
            self.click_selectable_item(self.locators.ITEM_LIST)
            active_elements = self.elements_are_visible(self.locators.ITEM_LIST_ACTIVE)
        elif tab == 'grid':
            self.element_is_visible(self.locators.TAB_GRID).click()
            self.click_selectable_item(self.locators.ITEM_GRID)
            active_elements = self.elements_are_visible(self.locators.ITEM_GRID_ACTIVE)
        active_list = []
        for element in active_elements:
            active_list.append(element.text)
        return active_list


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def change_size_resizable_box(self):
        locator = self.element_is_visible(self.locators.RESIZABLE_BOX)
        handle_locator = self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE)

        start_size = locator.get_attribute('style').replace(';', '')

        self.slide_action(handle_locator, -50, -50)
        min_size = locator.get_attribute('style').replace(';', '')

        self.slide_action(handle_locator, 350, 150)
        max_size = locator.get_attribute('style').replace(';', '')

        return start_size, min_size, max_size

    def change_size_resizable(self):
        size_before = self.element_is_present(self.locators.RESIZABLE).get_attribute('style')
        self.slide_action(self.element_is_present(self.locators.RESIZABLE_HANDLE), random.randint(-100, 100),
                          random.randint(-100, 100))
        size_after = self.element_is_present(self.locators.RESIZABLE).get_attribute('style')
        return size_before, size_after


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def check_drop_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        self.drag_and_drop(self.element_is_visible(self.locators.SIMPLE_TAB_DRAGGABLE),
                          self.element_is_visible(self.locators.SIMPLE_TAB_DROPPABLE))
        text_result = self.element_is_visible(self.locators.SIMPLE_TAB_DROPPABLE).text
        return text_result

    def check_drop_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()

        acceptable = self.element_is_visible(self.locators.ACCEPT_TAB_ACCEPTABLE)
        not_acceptable = self.element_is_visible(self.locators.ACCEPT_TAB_NOT_ACCEPTABLE)
        droppable = self.element_is_visible(self.locators.ACCEPT_TAB_DROPPABLE)

        self.drag_and_drop(not_acceptable, droppable)
        text_after_moving_not_acceptable = droppable.text
        self.drag_and_drop(acceptable, droppable)
        text_after_moving_acceptable = droppable.text

        return text_after_moving_not_acceptable, text_after_moving_acceptable

    def check_drop_prevent_propogation(self):
        self.element_is_visible(self.locators.PREVENT_PROPOGATION_TAB).click()

        drag_me = self.element_is_visible(self.locators.DRAG_ME)
        not_greedy_inner_box = self.element_is_visible(self.locators.NOT_GREEDY_DROP_INNER_BOX)
        greedy_inner_box = self.element_is_visible(self.locators.GREEDY_DROP_INNER_BOX)

        self.drag_and_drop(drag_me, not_greedy_inner_box)
        text_not_greedy_box = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX_TEXT).text
        text_not_greedy_inner_box =self.element_is_visible(self.locators.NOT_GREEDY_DROP_INNER_BOX_TEXT).text

        self.drag_and_drop(drag_me, greedy_inner_box)
        text_greedy_inner_box = self.element_is_visible(self.locators.GREEDY_DROP_INNER_BOX_TEXT).text
        text_greedy_box = self.element_is_visible(self.locators.GREEDY_DROP_BOX_TEXT).text

        return text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box

    def check_drop_revent_draggable(self, type_drag):
        drags = {
            'will_revert':
                {'revert': self.locators.WILL_REVERT},
            'not_revert':
                {'revert':self.locators.NOT_REVERT}
        }
        self.element_is_visible(self.locators.REVENT_DRAGGABLE_TAB).click()

        revert = self.element_is_visible(drags[type_drag]['revert'])
        drop_here = self.element_is_visible(self.locators.DROP_HERE)

        self.drag_and_drop(revert, drop_here)
        position_after_move = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_after_move, position_after_revert