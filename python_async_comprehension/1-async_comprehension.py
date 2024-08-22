#!/usr/bin/env python3
"""
This module contains the coroutine async_comprehension.
"""

import asyncio
from typing import List

# Importation relative du module 0-async_generator
import async_generator

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator 
    using an async comprehension.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    return [num async for num in async_generator()]
