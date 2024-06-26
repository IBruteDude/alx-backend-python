#!/usr/bin/env python3
""" Module for trying actual coroutines
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Wait for n random delays
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    results = []

    for task in tasks:
        task.add_done_callback(lambda task: results.append(task.result()))

    await asyncio.gather(*tasks)
    return results


if __name__ == '__main__':
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
