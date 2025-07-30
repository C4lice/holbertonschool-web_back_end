#!/usr/bin/env python3
"""
module à 1 fonction
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    faire la moyenne du temps d'exécution du code
    """
    return (asyncio.create_task(wait_random(max_delay)))
