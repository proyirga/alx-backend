#!/usr/bin/env python3
"""1-simple_pagination.py"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Args:
    page: int
    page_size: int

    Returns:
    tuple
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset


    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Args:
        page: int
        page_size: int
        
        Returns:
        List[List]
        """
        assert isinstance(page, int) and isinstance(page_size, int), "Both arguments must be integers."
        assert page > 0 and page_size > 0, "Both arguments must be greater than 0."
        
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        
        return dataset[start_index:end_index]

