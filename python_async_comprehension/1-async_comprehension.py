#!/usr/bin/env python3
"""
Asynchronous generator that produces random float values between 0 and 10.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collection of 10 random numbers using asynchronous calculation
    """
    return [i async for i in async_generator()]
