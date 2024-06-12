#!/usr/bin/env python3
""" Module for creating an async generator comprehension
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ create an async generator comprehension
    """
    return [i async for i in async_generator()]


if __name__ == '__main__':
    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
