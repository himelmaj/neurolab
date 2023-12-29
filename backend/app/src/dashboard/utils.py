
# This file contains utility functions for the dashboard.


# Paginate the data.
def get_paginated_data(query, page: int = None, size: int = None, count: int = None):
    max_page = (count + size - 1) // size
    return {
        "results": query,
        "info": {
            "pageNumber": page,
            "pageSize": size,
            "pages": max_page,
            "count": count,
        }
    }