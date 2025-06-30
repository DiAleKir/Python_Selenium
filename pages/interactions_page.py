import random

from locators.interactions_locators import SortablePageLocators, SelectablePageLocators
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