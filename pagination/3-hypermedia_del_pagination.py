#!/usr/bin/env python3
"""
Pagination hypermédia résistante aux suppressions
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Classe serveur permettant de paginer une base de données de prénoms populaires.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Ensemble de données indexé par la position de tri, en commençant par 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        renvoie un dict d'informations précieuses sur la page actuelle et la suivante
        """
        data_set = self.indexed_dataset()
        assert index < len(data_set)
        data = []
        loop = page_size
        i = 0
        while i < loop:
            try:
                data.append(data_set[index + i])
            except KeyError:
                loop += 1
            i += 1
        return {
            "index": index,
            "next_index": index + page_size,
            "page_size": page_size,
            "data": data,
        }
