#!/usr/bin/env python3
"""
This module provides a utility function that returns a tuple
containing a string and the square of a numeric value.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of a number.

    Args:
        k (str): The string key.
        v (int | float): A number to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string `k`,
                           and the second is the square of `v` as a float.
    """
    result: Tuple[str, float] = (k, v**2)
    return (result)
