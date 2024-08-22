#!/usr/bin/env python3
"""
Main module to test the async_generator coroutine.
"""

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    """
    Collects values from the async_generator coroutine and prints them.
    """
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

if __name__ == "__main__":
    asyncio.run(print_yielded_values())
