import random

from locators.interactions_locators import SortablePageLocators
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
        return order_before, order_after, 'The order has not been changed'

    def change_grid_order(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_sortable_items(self.locators.ITEM_GRID)
        item_list = random.sample(self.elements_are_visible(self.locators.ITEM_GRID), k=2)
        self.drag_and_drop(item_list[0], item_list[1])
        order_after = self.get_sortable_items(self.locators.ITEM_GRID)
        return order_before, order_after, 'The order has not been changed'