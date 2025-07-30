#!/usr/bin/env python3
"""
Générateur asynchrone qui produit des valeurs flottantes aléatoires entre 0 et 10.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collecte de 10 nombres aléatoires à l'aide d'un calcul asynchrone
    """
    return [i async for i in async_generator()]
