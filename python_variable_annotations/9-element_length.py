#!/usr/bin/env python3
"""
This module provides a utility function for summing elements
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function provides"""
    return [(i, len(i)) for i in lst]
