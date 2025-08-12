#!/usr/bin/env python3

"""
module avec une fonction page 1
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    la fonction renvoie le premier et le dernier index de la page
    dépend de la taille de la page
    """
    result: Tuple = ((page - 1) * page_size, page * page_size)
    return result
