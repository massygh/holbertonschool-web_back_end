#!/usr/bin/env python3
"""
This module contains the coroutine async_generator which generates random
numbers asynchronously.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that generates 10 random floating-point numbers asynchronously
    between 0 and 10, with a delay of 1 second between each.

    Yields:
        float: Random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
