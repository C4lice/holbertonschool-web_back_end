#!/usr/bin/env python3
"""
module à 1 fonction
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    faire la moyenne du temps d'exécution du code
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    execution_time = end - start
    return (execution_time / n)
