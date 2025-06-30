from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


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


    class TestResizable:

        def test_resizable_box(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            start_size, min_size, max_size = resizable_page.change_size_resizable_box()
            assert start_size == 'width: 200px height: 200px', 'Start size not equal to 200px, 200px'
            assert min_size == 'width: 150px height: 150px', 'Minimum size not equal to 150px, 150px'
            assert max_size == 'width: 500px height: 300px', 'Maximum size not equal to 500px, 300px'

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            size_before, size_after = resizable_page.change_size_resizable()
            assert size_before != size_after, 'The size has not changed'