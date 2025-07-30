#!/usr/bin/env python3
"""
Générateur asynchrone qui produit des valeurs flottantes aléatoires entre 0 et 10.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Boucle 10 fois, en attendant à chaque fois 1 seconde de manière asynchrone,
    puis donne une valeur flottante aléatoire entre 0 et 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
