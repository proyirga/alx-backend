#!/usr/bin/env python3
"""2-hypermedia_pagination.py"""


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Args:
        page: int
        page_size: int
        
        Returns:
        dict
        """
        assert isinstance(page, int) and isinstance(page_size, int), "Both arguments must be integers."
        assert page > 0 and page_size > 0, "Both arguments must be greater than 0."
        
        dataset = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        
        return {
            "page_size": len(dataset),
            "page": page,
            "data": dataset,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }   
