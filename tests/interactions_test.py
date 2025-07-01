from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


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


    class TestDroppable:

        def test_simple_tab(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text_result = droppable_page.check_drop_simple()
            assert text_result == 'Dropped!', 'The element has not been dropped'

        def test_accept_tab(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_acceptable, acceptable = droppable_page.check_drop_accept()
            assert not_acceptable == 'Drop here', 'The element has been accepted'
            assert acceptable == 'Dropped!', 'The element has not been accepted'

        def test_prevent_propogation(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.check_drop_prevent_propogation()
            assert not_greedy == 'Dropped!', 'The text has not been changed'
            assert not_greedy_inner == 'Dropped!', 'The text has not been changed'
            assert greedy == 'Outer droppable', 'The text has been changed'
            assert greedy_inner == 'Dropped!', 'The text has not been changed'

        def test_revert_draggable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            position_after_move, position_after_revert = droppable_page.check_drop_revent_draggable('will_revert')
            assert position_after_move != position_after_revert, 'The element has not returned to original position'

        def test_not_revert_draggable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            position_after_move, position_after_revert = droppable_page.check_drop_revent_draggable('not_revert')
            assert position_after_move == position_after_revert, 'The element returned to original position'