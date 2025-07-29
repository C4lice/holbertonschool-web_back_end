#!/usr/bin/env python3
"""
This module provides a utility function for summing elements
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Calculate the sum of all elements in a list of floats.
    """
    def mul(x: float) -> float:
        return x * multiplier
    return mul
