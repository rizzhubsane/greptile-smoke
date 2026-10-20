from paging import resources_on_page


def test_full_page():
    assert resources_on_page(100, 24, 1) == 24


def test_last_page_is_short():
    assert resources_on_page(50, 24, 3) == 2


def test_page_past_the_end_is_empty():
    assert resources_on_page(50, 24, 4) == 0
