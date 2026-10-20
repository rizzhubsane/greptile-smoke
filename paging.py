def resources_on_page(total: int, page_size: int, page: int) -> int:
    """How many catalog rows belong on this 1-based page."""
    if page < 1 or page_size < 1 or total < 0:
        return 0
    start = (page - 1) * page_size
    if start >= total:
        return 0
    return min(page_size, total - start)
