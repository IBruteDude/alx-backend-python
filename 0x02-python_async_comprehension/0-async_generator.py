#!/usr/bin/env python3
""" Module for creating an async generator
"""
import asyncio
from typing import AsyncGenerator
from random import uniform


async def async_generator() -> AsyncGenerator[float, None]:
    """ yield 10 random generated numbers
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)


if __name__ == '__main__':
    async_generator = __import__('0-async_generator').async_generator

    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
