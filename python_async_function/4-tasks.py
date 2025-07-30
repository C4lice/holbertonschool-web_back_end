#!/usr/bin/env python3
"""
module with 1 function
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    wait for a random time n time
    """
    tasks = [task_wait_random(max_delay) for i in range(n)]
    result: List[float] = []
    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        result.append(delay)
    return (result)
