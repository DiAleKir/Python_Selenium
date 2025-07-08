import allure

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


@allure.suite("Interactions")
class TestInteractions:

    @allure.feature('Sortable')
    class TestSortable:

        @allure.title('Check the sorting of the list')
        def test_list_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_list_order()
            assert order_before != order_after, 'The order has not been changed'

        @allure.title('Check the sorting of the grid')
        def test_frid_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_grid_order()
            assert order_before != order_after, 'The order has not been changed'


    @allure.feature('Selectable')
    class TestSelectable:
        @allure.title('Check the selectable of items in the list')
        def test_list_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            active_elements = selectable_page.select_item('list')
            assert len(active_elements) > 0, 'The elements were not selected'

        @allure.title('Check the selectable of items in the grid')
        def test_grid_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            active_elements = selectable_page.select_item('grid')
            assert len(active_elements) > 0, 'The elements were not selected'


    @allure.feature('Resizable')
    class TestResizable:

        @allure.title('Check the box size change')
        def test_resizable_box(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            start_size, min_size, max_size = resizable_page.change_size_resizable_box()
            assert start_size == 'width: 200px height: 200px', 'Start size not equal to 200px, 200px'
            assert min_size == 'width: 150px height: 150px', 'Minimum size not equal to 150px, 150px'
            assert max_size == 'width: 500px height: 300px', 'Maximum size not equal to 500px, 300px'

        @allure.title('Check the window size change')
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            size_before, size_after = resizable_page.change_size_resizable()
            assert size_before != size_after, 'The size has not changed'


    @allure.feature('Droppable')
    class TestDroppable:

        @allure.title('Check the movement of the element in the box')
        def test_simple_tab(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text_result = droppable_page.check_drop_simple()
            assert text_result == 'Dropped!', 'The element has not been dropped'

        @allure.title('Check the moving the acceptable and not acceptable elements in the box')
        def test_accept_tab(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_acceptable, acceptable = droppable_page.check_drop_accept()
            assert not_acceptable == 'Drop here', 'The element has been accepted'
            assert acceptable == 'Dropped!', 'The element has not been accepted'

        @allure.title('Check the moving of the element to the greedy and not greedy boxes')
        def test_prevent_propogation(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.check_drop_prevent_propogation()
            assert not_greedy == 'Dropped!', 'The text has not been changed'
            assert not_greedy_inner == 'Dropped!', 'The text has not been changed'
            assert greedy == 'Outer droppable', 'The text has been changed'
            assert greedy_inner == 'Dropped!', 'The text has not been changed'

        @allure.title('Check the movement of a revert element')
        def test_revert_draggable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            position_after_move, position_after_revert = droppable_page.check_drop_revent_draggable('will_revert')
            assert position_after_move != position_after_revert, 'The element has not returned to original position'

        @allure.title('Check the movement of a not revert element')
        def test_not_revert_draggable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            position_after_move, position_after_revert = droppable_page.check_drop_revent_draggable('not_revert')
            assert position_after_move == position_after_revert, 'The element returned to original position'