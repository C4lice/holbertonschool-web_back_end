#!/usr/bin/env python3
"""
This module provides a utility function for summing elements
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all elements in a list of floats.
    """
    result: float = 0
    for i in range(len(input_list)):
        result += input_list[i]
    return (result)
