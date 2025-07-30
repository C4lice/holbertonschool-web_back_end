#!/usr/bin/env python3
"""
Asynchronous generator that produces random float values between 0 and 10.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times, waiting asynchronously for 1 second each time,
    then gives a random float value between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
