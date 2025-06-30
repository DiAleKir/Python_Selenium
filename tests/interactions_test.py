from pages.interactions_page import SortablePage, SelectablePage


class TestInteractions:

    class TestSortable:

        def test_list_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_list_order()
            assert order_before != order_after, 'The order has not been changed'

        def test_frid_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_grid_order()
            assert order_before != order_after, 'The order has not been changed'


    class TestSelectable:

        def test_list_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            active_elements = selectable_page.select_item('list')
            assert len(active_elements) > 0, 'The elements were not selected'

        def test_grid_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            active_elements = selectable_page.select_item('grid')
            assert len(active_elements) > 0, 'The elements were not selected'