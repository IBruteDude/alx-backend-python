#!/usr/bin/env python3
""" Module for trying actual coroutines
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Wait for n tasks with random delays
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    results = []

    for task in tasks:
        task.add_done_callback(lambda task: results.append(task.result()))

    await asyncio.gather(*tasks)
    return results


if __name__ == '__main__':
    import asyncio

    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
