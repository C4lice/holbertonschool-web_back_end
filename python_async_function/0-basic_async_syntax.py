#!/usr/bin/env python3
"""
module à 1 fonction
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    attendre une durée aléatoire
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return (delay)
