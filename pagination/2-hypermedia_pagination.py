#!/usr/bin/env python3

"""
module avec 1 classe
"""
import csv
import math
from typing import List, Tuple, Dict


class Server:
    """
    Classe serveur permettant de paginer une base de données de prénoms populaires.
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
        la fonction renvoie le premier et le dernier index de la page
        dépend de la taille de la page
        """
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0
        result = []
        data_set: List[List] = self.dataset()
        index: Tuple = self.index_range(page, page_size)
        try:
            for i in range(page_size):
                result.append(data_set[index[0] + i])
        except IndexError:
            return []
        return result

    def index_range(self, page: int, page_size: int) -> Tuple:
        """
        la fonction renvoie le premier et le dernier index de la page
        dépend de la taille de la page
        """
        result: Tuple = ((page - 1) * page_size, page * page_size)
        return result

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        la fonction renvoie un dict de données utiles
        """
        total_page = len(self.dataset())
        data = self.get_page(page, page_size)
        if (page == 1):
            prev_page = None
        else:
            prev_page = page - 1
        if (page >= total_page or len(data) == 0):
            next_page = None
        else:
            next_page = page + 1
        result: Dict = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": math.ceil(total_page / page_size)
        }
        return result
