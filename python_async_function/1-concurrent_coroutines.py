#!/usr/bin/env python3
"""
module à 1 fonction
"""
from typing import List
import asyncio


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    attendre un temps aléatoire n temps
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    tasks = [wait_random(max_delay) for i in range(n)]
    result: List[float] = []
    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        result.append(delay)
    return (result)
