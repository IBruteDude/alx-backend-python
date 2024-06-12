#!/usr/bin/env python3
""" Module for time measuring coroutine
"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure the running time for the generator coroutines
    """
    start = time()
    await asyncio.gather(
        *(async_comprehension() for _ in range(4))
    )
    end = time()
    return (end - start)


if __name__ == '__main__':
    async def main():
        return await(measure_runtime())

    print(
        asyncio.run(main())
    )
